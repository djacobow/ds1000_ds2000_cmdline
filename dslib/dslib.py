#!/usr/bin/env python3

import datetime
import itertools
import math
import re
import socket

from . import rigol_config
from . import arg_wrangler

def wrap1(param, func):
    def wrap2(*args, **kwargs):
        return func(param, *args, **kwargs)
    return wrap2

class RigolScope(object):
    def __init__(self, ip=None, personality='ds1k'):
        self.personality = personality
        self.configs = rigol_config.RIGOL_CONFIG.get(personality)
        if self.configs is None:
            raise Exception(f'Do not know how to talk to {personality} type scope.')

        for (gname,gconfig) in self.configs.items():
            for name, config in gconfig.get('commands',{}).items():
                config['name'] = name
                wrapped_fn = wrap1(config, self.generic_func_wrapper)
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
                if aval is not None and aval is not False:
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

        def makeMetavars(argspecs):
            num_argspecs = len(argspecs)
            if num_argspecs == 0:
                return ''

            metametavars = []
            for argspec_idx in range(num_argspecs):
                argspec = argspecs[argspec_idx]
                final = argspec_idx == num_argspecs-1
                mmv = argspec.metametavar()
                # if there is only on arg and it is optional,
                # then argparse will add the brackets. But if there
                # is more than one, we need to add them because 
                # as far as argparse is concerned, they are all just
                # shmooshed together as one
                if final and num_argspecs != 1:
                    mmv = ''.join(['[',mmv,']'])
                metametavars.append(mmv)

            metavar = None
            if len(metametavars):
                metavar = ':'.join(metametavars)

            return metavar

        def enumerate_arg_choices(argspecs):
            choices = None
            set_choices_list = [ v.choices() for v in argspecs ]
            set_choices = None
            if not None in set_choices_list:
                set_choices = [
                    ':'.join(
                        [str(x) for x in t]
                    ) for t in itertools.product(*set_choices_list)
                ]

            get_choices_list = set_choices_list
            get_choices = None
            if len(get_choices_list):
                get_choices_list.pop()
            if len(get_choices_list) and not None in get_choices_list:
                get_choices = [
                    ':'.join(
                        [str(x) for x in t]
                    ) for t in itertools.product(*get_choices_list)
                ]

            if get_choices is not None and set_choices is not None:
                choices = set_choices + get_choices
            return choices


        def make_parseargs_generic(parser_group, gconfig):
            for name, config in gconfig.get('commands',{}).items():
                aname = re.sub(r'_','-',name)
                argspecs = config.get('argspecs',())
                num_argspecs = len(argspecs)
                self.arg_handlers[name] = getattr(self, name)

                flag_name = '--' + aname
                if num_argspecs == 0:
                    parser_group.add_argument(
                        flag_name,
                        action='store_true',
                        help=config.get('help'),
                    ) 

                else:
                    choices = enumerate_arg_choices(argspecs)
                    metavar = makeMetavars(argspecs)

                    if num_argspecs == 1:
                        parser_group.add_argument(
                            flag_name,
                            nargs='?',
                            metavar=metavar,
                            const='',
                            type=str,
                            choices=choices,
                            help=config.get('help',None), 
                        )
                    else:
                        parser_group.add_argument(
                            flag_name,
                            nargs=1,
                            metavar=metavar,
                            type=str,
                            choices=choices,
                            help=config.get('help',None), 
                        )


        parser_groups = {}

        for gname, gconfig in self.configs.items():
            if not gname in parser_groups:
                parser_group = parser.add_argument_group(
                    title=gconfig.get('name',''),
                    description=gconfig.get('description',None),
                )
                parser_groups[gname] = parser_group
            else: 
                parser_group = parser_groups[gname]

            make_parseargs_generic(parser_group, gconfig)


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

    def _wrapped_0_argument_function(self, config):
        cmd = config.get('cmd')
        if cmd is None:
            raise Exception('Missing command specification')
        else:
            is_query = re.search(r'.*\?$', cmd)    
            if is_query:
                return self.cmd(cmd)
            else:
                return self._cmdo(cmd)


    def generic_func_wrapper(self, config, *args):
        wrangled = arg_wrangler.ArgumentWrangler(config, args)

        func = config.get('func')
        cmd  = config.get('cmd')

        # dispatch the command depending on the type
        if func is not None:
           if not callable(func):
               raise Exception(f'For function {name}: {func} is not callable')
           return config['func'](self, args)
        elif cmd is not None:
            if wrangled.isQuery():
                return self.cmd(cmd)
            else:
                return self._cmdo(cmd)
        else:
            if wrangled.isQuery():
                return wrangled.convert_to_rtype(config, self.cmd(config.get('q_str').format(**wrangled.argdict())))
            else:
               self._cmdo(config.get('set_str').format(**wrangled.argdict()))


if __name__ == '__main__':
    pass

