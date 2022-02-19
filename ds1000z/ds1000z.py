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
            for name, config in self.configs.get(gc[0],{}).items():
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
        query_group   = parser.add_argument_group(
            title="Global Getters",
            description='Queryable global settings',
        )
        channel_group = parser.add_argument_group(
            title="Channel Setter/ Getters",
            description='Setting that pertain to individual channels. Use channel:value to set the value, or just channel to read it'
        )
        action_group  = parser.add_argument_group(
            title='Actions',
            description='Global actions'
        )
        sg_group  = parser.add_argument_group(
            title='Setter / Getters',
            description='Various settings that can be set or read back'
        )
        self.arg_handlers = {}

        for name, config in self.configs.get('simple_0_args',{}).items():
            aname = re.sub(r'_','-',name)
            is_query = re.search(r'.*\?$',config['cmd'])
            self.arg_handlers[name] = getattr(self, name)
            if is_query:
                query_group.add_argument(
                    '--' + aname,
                    default=None,
                    action='store_true',
                ) 
            else:
                action_group.add_argument(
                    '--' + aname,
                    default=None,
                    action='store_true',
                ) 

        for name, config in self.configs.get('simple_1_args',{}).items():
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
                choices = tuple(list(choices) + [''])
                const = ''

            sg_group.add_argument(
                '--' + aname + '',
                nargs='?',
                const=const,
                default=None,
                type=ttype,
                choices=choices,
                help=config.get('help',None), 
            )


        for name, config in self.configs.get('simple_2_args',{}).items():
            aname = re.sub(r'_','-',name)
            validators = config.get('validators',())
            num_validators = len(validators)
            self.arg_handlers[name] = getattr(self, name)

            if num_validators != 2:
               raise Exception(f'Error config for {aname} is wrong; should have exactl 2 validators')

            choices_0 = None
            choices_1 = None
            choices = None
            if isinstance(validators[0][1],(list,tuple)):
                choices_0 = validators[0][1] 
            if isinstance(validators[1][1],(list,tuple)):
                choices_1 = validators[1][1] 
            if choices_0 is not None and choices_1 is not None:
                choices = []
                for ch0 in choices_0:
                    choices += [ f'{ch0}:{ch1}' for ch1 in choices_1 ]

            channel_group.add_argument(
                '--' + aname,
                nargs='?',
                metavar='ch#:value',
                const='',
                type=str,
                choices=choices,
                help=config.get('help',None), 
            )

    def _cmdo(self, c):
        s = c + '\n'
        b = s.encode('utf-8',errors='replace')
        self.s.send(b)
        print('-->',b)
  
    def _cmdi(self):
        r = self.sr.readline().decode('ascii').strip()
        print('<--',r)
        return r

    def cmd(self, c):
        self._cmdo(c)
        return self._cmdi()

    def screenCap(self, fn=None):
        if fn is None or not len(fn):
            now = datetime.datetime.now().isoformat()
            now = re.sub(r'\.\d+','',now)
            now = re.sub(r'[\-\:]','_',now)
            fn = f'rigol_cap_{now}.png'
        self._cmdo(':DISPLAY:DATA? ON,OFF,PNG')
        h0 = self.sr.read(1) # should be literal '#'
        h1 = self.sr.read(1)
        size_size = int(h1)
        h2 = self.sr.read(1) # what does this do/mean?
        p = self.sr.read(size_size-1)
        size = int(p.decode('ascii'))
        d = self.sr.read(size)
        with open(fn,'wb') as ofh:
            ofh.write(d)

        endl = self.sr.read(1)
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

        if vcount != 2:
            raise Exception(f'configuration error; expect exactly 2 validators ({vcount})')

        subargs = []

        if acount == 2:
            subargs = args
        elif acount == 1:
            subargs = args[0].split(':')
            converted_subargs = []
            for i in range(len(subargs)):
                converted_subargs.append(self.convert_to_type(validators[i][0][0], subargs[i]))
            subargs = converted_subargs
        self.expand_cmd_strs(config)

        is_query = len(subargs) == 1

        d = {}
        self.validate(subargs[0], config['validators'][0])
        d['a0'] = subargs[0]

        if not is_query:
            self.validate(subargs[1], config['validators'][1])
            d['a1'] = subargs[1]
         
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

