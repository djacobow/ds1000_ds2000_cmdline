#!/usr/bin/env python3
import re

class ArgSpec(object):

    def __init__(self):
        pass

    def metametavar(self):
        return None

    def choices(self):
        return None

    def ttype(self):
        return self.types[0]

class OptionArgSpec(ArgSpec):
    def __init__(self, l, types=(str,)):
        self.types = types if isinstance(types,(list,tuple,)) else tuple([types])
        self.options = l

    def validate(self, x):
        if not isinstance(x, self.types):
            return (False, f'argument provided ({x}) of type {type(x)} must be one of: {", ".join([repr(x) for x in self.types])}')
        if isinstance(x, str):
           x = x.lower()
        # print('x',x,'type',type(x))
        if not x in self.options: 
            return (False, f'argument provided ({x}) must be one of {", ".join([repr(x) for x in self.options])}')
        return (True, None)

    def metametavar(self):
        return f"{{{','.join([str(x) for x in self.options])}}}"

    def choices(self):
        return self.options


class TypeArgSpec(ArgSpec):
    def __init__(self, types=(float,)):
        self.types = types if isinstance(types,(list,tuple)) else (types,)

    def validate(self, x):
        if not isinstance(x,self.types):
            return (False, f'Argument is of type {type(x)}; but one of {repr(self.types)} required')
        return (True, None)
 
    def metametavar(self):
        tstr = re.sub(f',$','',re.sub(r'(\(|\)|class|\'|\s)','',repr(self.types)))
        return f'{tstr}'


class RangeArgSpec(ArgSpec):
    def __init__(self, rmin, rmax, types=(float,)):
        if rmax < rmin:
            (rmin, rmax) = (rmax, rmin)
        self.rmin = rmin
        self.rmax = rmax
        self.types = types if isinstance(types,(list,tuple)) else (types,)

    def validate(self, x):
        if not isinstance(x,self.types):
            return (False, f'Argument is of type {type(x)}; but one of {repr(self.types)} required')

        if not (self.rmin <= x and x <= self.rmax):
            return (False, f'Argument is ({x}) not in range [{self.rmin},{self.rmax}]')
        return (True, None)

    def metametavar(self):
        tstr = re.sub(f',$','',re.sub(r'(\(|\)|class|\'|\s)','',repr(self.types)))
        return f'{tstr} in range [{self.rmin},{self.rmax}]'



class FunctionArgSpec(ArgSpec):
    def __init__(self, func, types=(str,), message=''):
        self.func = func
        self.message = message
        self.types = types if isinstance(types,(list,tuple,)) else tuple([types])

    def validate(self, x):
        if not isinstance(x,self.types):
            return (False, f'Argument is of type {type(x)}; but one of {repr(self.types)} required')
      
        ok = self.func(x)
        if not ok:
            return (False, f'Argument {x} did not pass Func {repr(self.func)}')
        return (True, None)

    def metametavar(self):
        return self.message

if __name__ == '__main__':

    if False:
        w = OptionArgSpec(('x','y','z'))
        w.validate('x')
        print(w.metametavar())
        w.validate('a')

    if True:
        x = RangeArgSpec(-10,10,types=(int,float))
        x.validate(0)
        x.validate(10)
        print(x.metametavar())
        x.validate(11)
