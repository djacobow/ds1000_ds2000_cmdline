#!/usr/bin/env python3

import datetime
import math
import re
import socket

from . import rigol_config

def wrap1(param, func):
    # print(f'in wrap1, param: {param}, func: {func}')
    def wrap3(*args, **kwargs):
        # print(f'in wrap3, param: {param}, func: {func}, args: {",".join([str(x) for x in args])}')
        return func(param, *args, **kwargs)
    return wrap3

class RigolDS1000z(object):
    def __init__(self, ip=None):
        self.configs = rigol_config.RIGOL_CONFIG 

        groups_config = (
            ('simple_2_args', self._simple_2_arg),
            ('simple_1_args', self._simple_1_arg),
            ('simple_0_args', self._simple_0_arg),
        )
        for gc in groups_config:
            for gname, gconfig in self.configs.get(gc[0],{}).items():
                for name, config in gconfig.get('commands',{}).items():
                    wrapped_fn = wrap1(config, gc[1])
                    setattr(self, name, wrapped_fn)

        if ip is not None:
            self.connect(ip)

    def connect(self, ip):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 5555))
        self.s = s
        self.sr = s.makefile('rb',errors='replace')

    def dispatchArgs(self, args):
        adict = vars(args)
        rdict = {}
        for aname, aval in adict.items():
            # print('aname',aname,'aval',aval)
            # print(self.arg_handlers.keys())
            if aname in self.arg_handlers:
                #print('we know this')
                if aval is not None:
                    # print('aname',aname,'aval',aval)
                    if aval == True:
                        rv = self.arg_handlers[aname]()
                    elif isinstance(aval,(list,tuple)):
                        rv = self.arg_handlers[aname](*aval)
                    else:
                        rv= self.arg_handlers[aname](aval)
                    if rv is not None:
                        rdict[aname] = rv
        return rdict

    def makeArgs(self, parser):
        self.arg_handlers = {}

        def make_simple_0_args(parser_group, gconfig):
            for name, config in gconfig.get('commands',{}).items():
                aname = re.sub(r'_','-',name)
                is_query = re.search(r'.*\?$',config['cmd'])
                self.arg_handlers[name] = getattr(self, name)
                parser_group.add_argument(
                    '--' + aname,
                    default=None,
                    action='store_true',
                ) 

        def make_simple_1_args(parser_group, gconfig):
            for name, config in gconfig.get('commands',{}).items():
                
                aname = re.sub(r'_','-',name)
                validators = config.get('validators',())
                num_validators = len(validators)
    
                if num_validators != 1:
                    print(validators)
                    raise Exception(f'One-arg functions should have only one arg: {name} {num_validators}!')
    
                self.arg_handlers[name + '']       = getattr(self, name)
    
                choices = None
                ttype = None
                if isinstance(validators[0][1],(list,tuple)):
                    choices = validators[0][1] 
                if isinstance(validators[0][0],(list,tuple)):
                    ttype = validators[0][0][0]
                elif isinstance(validators[0][0],(type,)):
                    ttype = validators[0][0]
    
                const = False
                if ttype == float:
                    const = float('Nan')
                elif ttype == int:
                    const = float('Nan')
                else:
                    if choices is not None:
                        choices = tuple(list(choices) + [''])
                    const = ''
    
                parser_group.add_argument(
                    '--' + aname + '',
                    nargs='?',
                    const=const,
                    default=None,
                    type=ttype,
                    choices=choices,
                    help=config.get('help',None), 
                )

        def make_simple_2_args(parser_group, gconfig):
            for name, config in gconfig.get('commands',{}).items():
                aname = re.sub(r'_','-',name)
                validators = config.get('validators',())
                num_validators = len(validators)
                self.arg_handlers[name] = getattr(self, name)
    
                if num_validators < 2:
                   raise Exception(f'Error config for {aname} is wrong; should have at least 2 validators')
    
                choices_0 = None
                choices_1 = None
                choices = None
                if num_validators == 2:
                    if isinstance(validators[0][1],(list,tuple)):
                        choices_0 = validators[0][1] 
                    if isinstance(validators[1][1],(list,tuple)):
                        choices_1 = validators[1][1] 
                    if choices_0 is not None and choices_1 is not None:
                        choices = []
                        for ch0 in choices_0:
                            choices += [ f'{ch0}' ]
                            choices += [ f'{ch0}:{ch1}' for ch1 in choices_1 ]

                elif num_validators == 3:
                    metavar='dec#:ch#:value or dec#:ch#'
   
                metametavars = []
                for validator_idx in range(num_validators):
                    validator = validators[validator_idx]
                    final = validator_idx = num_validators-1
                    if  isinstance(validator[1],(list,tuple)):
                        l = validator[1]
                        metametavars.append(f"{{{','.join([str(x) for x in l])}}}")
                    else:
                        l = [ re.sub(r'(\'|\s|class)','',str(x)) for x in validator[0] ]
                        s = f"{'|'.join(l)}"
                        if final:
                            s = ''.join(['[',s,']'])
                        metametavars.append(s)

                metavar = None
                if len(metametavars):
                    metavar = ':'.join(metametavars)

                parser_group.add_argument(
                    '--' + aname,
                    nargs='?',
                    metavar=metavar,
                    const='',
                    type=str,
                    choices=choices,
                    help=config.get('help',None), 
                )

        command_types = (
            ('simple_0_args', make_simple_0_args),
            ('simple_1_args', make_simple_1_args),
            ('simple_2_args', make_simple_2_args),
        ) 

        parser_groups = {}

        for command_type in command_types:
            for gname, gconfig in self.configs.get(command_type[0],{}).items():

                if not gname in parser_groups:
                    parser_group = parser.add_argument_group(
                        title=gconfig.get('name',''),
                        description=gconfig.get('description',None),
                    )
                    parser_groups[gname] = parser_group
                else: 
                    parser_group = parser_groups[gname]

                command_type[1](parser_group, gconfig)


    def _cmdo(self, c, bdata=None):
        if bdata is None:
            s = c + '\n'
            b = s.encode('utf-8',errors='replace')
            self.s.send(b)
            print('-->',b)
        else:
            b = (c + ' ').encode('utf-8',errors='replace')
            b += bdata
            self.s.send(b)
            print('-->',c)
  
    def _cmdi(self):
        r = self.sr.readline().decode('ascii').strip()
        print('<--',r)
        return r

    def cmd(self, c):
        self._cmdo(c)
        return self._cmdi()

    def fileSafeDate(self):
        now = datetime.datetime.now().isoformat()
        now = re.sub(r'\.\d+','',now)
        now = re.sub(r'[\-\:]','_',now)
        return now

    def slurpRigolBlob(self):
        h0 = self.sr.read(1) # should be literal '#'
        h1 = self.sr.read(1)
        size_size = int(h1)
        h2 = self.sr.read(1) # what does this do/mean?
        p = self.sr.read(size_size-1)
        size = int(p.decode('ascii'))
        d = self.sr.read(size)
        endl = self.sr.read(1)
        return d, h0 + h1 + h2 + p + d + endl
 
    def restoreSetup(self, fn=None):
        if fn is None:
           raise Exception(f'File name is required to restore settings')
        d = None
        with open(fn, 'rb') as ifh:
            d = ifh.read()
        if d is None:
           raise Exception(f'Did not read any setup data from file')

        self._cmdo(':SYST:SET', d)
        return fn

    def saveSetup(self, fn=None):
        if fn is None or not len(fn):
            now = self.fileSafeDate()
            fn = f'rigol_setup_{now}.dat'
        self._cmdo(':SYST:SET?')
        inner, whole = self.slurpRigolBlob()
        with open(fn,'wb') as ofh:
            ofh.write(whole)
        return fn

    def screenCap(self, fn=None):
        if fn is None or not len(fn):
            now = self.fileSafeDate()
            fn = f'rigol_cap_{now}.png'
        self._cmdo(':DISPLAY:DATA? ON,OFF,PNG')
        inner, whole = self.slurpRigolBlob()
        with open(fn,'wb') as ofh:
            ofh.write(inner)
        return fn

    def _simple_0_arg(self, config):
        cmd = config.get('cmd')
        if cmd is None:
            raise Exception('Missing command specification')
        else:
            is_query = re.search(r'.*\?$', cmd)    
            if is_query:
                return self.cmd(cmd)
            else:
                return self._cmdo(cmd)

    def expand_cmd_strs(self, config):
        base_str = config.get('base_str')
        if config.get('q_str') is None:
            if base_str is None:
               raise Exception('Either q_str or base_str must be set')
            else:
               config['q_str'] = base_str + '?'

        if config.get('set_str') is None:
            if base_str is None:
               raise Exception('Either set_str or base_str must be set')
            else:
               config['set_str'] = base_str + ' {a0}'

    def convert_to_type(self, tt, r_raw):
        if tt=='float' or tt==float:
            return float(r_raw)
        elif tt=='int' or tt==int:
            return int(r_raw)
        return r_raw

    def convert_to_rtype(self, config, r_raw):
        return self.convert_to_type(config.get('rtype','str'), r_raw)

    def validate(self, val, validator):
        allowed_types = validator[0]
        if not isinstance(val, allowed_types):
            raise Exception(f'Argument must be of type: {", ".join([repr(x) for x in allowed_types])}')

        validator_fn = validator[1]
        if validator_fn is None:
            pass 
        elif callable(validator_fn):
            ok = validator_fn(val)
            if ok is not None and not ok:
                raise Exception(f'Argument rejected')
                return
        elif isinstance(validator_fn,(list,tuple)):
            if isinstance(val, str):
                val = val.lower()
                if not val in validator_fn:
                   raise Exception(f'argument must be one of {", ".join(validator_fn)}')
                   return

    def _simple_2_arg(self, config, *args):
        acount = len(args)
        validators = config.get('validators',())
        vcount = len(validators)

        if vcount < 2:
            raise Exception(f'configuration error; expect at leat 2 validators ({vcount})')

        subargs = []

        if acount == vcount:
            subargs = args
        elif acount == 1:
            subargs = args[0].split(':')
            converted_subargs = []
            for i in range(len(subargs)):
                converted_subargs.append(self.convert_to_type(validators[i][0][0], subargs[i]))
            subargs = converted_subargs
        self.expand_cmd_strs(config)

        is_query = len(subargs) < vcount

        d = { f'a{i}' : subargs[i] for i in range(len(subargs)) }

        for i in range(len(subargs)):
            self.validate(subargs[i], config['validators'][i])

        if is_query:
            return self.convert_to_rtype(config, self.cmd(config.get('q_str').format(**d)))
        else:
           self._cmdo(config.get('set_str').format(**d))



    def _simple_1_arg(self, config, *args):
        acount = len(args)
        validators = config.get('validators',())
        vcount = len(validators)

        if vcount > 1:
            raise Exception(f'configuration error; too many validators ({vcount})')
        if acount > 1:
            raise Exception(f'configuration error; too many argument ({acount})')

        is_query = False
        if acount == 0: 
            is_query = True
        elif isinstance(args[0],float) and math.isnan(args[0]):
            is_query = True
        elif isinstance(args[0],str) and len(args[0]) == 0:
            is_query = True

        self.expand_cmd_strs(config)

        d = {}
        if not is_query:
            in_arg = args[0]
            validator = validators[0]
            self.validate(in_arg, validator)
            d['a0'] = in_arg
            self._cmdo(config.get('set_str').format(**d))

        else:
            return self.convert_to_rtype(config, self.cmd(config.get('q_str').format(**d)))

if __name__ == '__main__':
    pass
