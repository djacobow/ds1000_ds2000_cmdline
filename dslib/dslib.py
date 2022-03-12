#!/usr/bin/env python3

import datetime
import math
import re
import socket

from . import rigol_config
from . import arg_wrangler
from . import parser_elaborator

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


    def addArgs(self, parser):
        self.arg_handlers = parser_elaborator.elaborateParser(parser, self.configs, self)

    def _cmdo(self, c, bdata=None):
        if bdata is None:
            s = c + '\n'
            b = s.encode('utf-8',errors='replace')
            self.s.send(b)
            #print('-->',b)
        else:
            b = (c + ' ').encode('utf-8',errors='replace')
            b += bdata
            self.s.send(b)
            #print('-->',c)
  
    def _cmdi(self):
        r = self.sr.readline().decode('ascii').strip()
        #print('<--',r)
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
           return config['func'](self, wrangled.args())
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

