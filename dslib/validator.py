#!/usr/bin/env python3
import re

class Validator(object):

    def __init__(self):
        pass

    def metametavar(self):
        return None

    def choices(self):
        return None

    def ttype(self):
        return self.types[0]

class OptionValidator(Validator):
    def __init__(self, l, types=(str,)):
        self.types = types if isinstance(types,(list,tuple,)) else tuple([types])
        self.options = l

    def validate(self, x):
        if not isinstance(x, self.types):
            raise Exception(f'argument provided ({x}) of type {type(x)} must be one of: {", ".join(self.types)}')
            return False
        if isinstance(x, str):
           x = x.lower()
        if not x in self.options: 
            raise Exception(f'argument provided ({x}) must be one of {", ".join(self.options)}')
            return False
        return True

    def metametavar(self):
        return f"{{{','.join([str(x) for x in self.options])}}}"

    def choicces(self):
        return self.l


class TypeValidator(Validator):
    def __init__(self, types=(float,)):
        self.types = types if isinstance(types,(list,tuple)) else (types,)

    def validate(self, x):
        if not isinstance(x,self.types):
            raise Exception(f'Argument is of type {type(x)}; but one of {repr(self.types)} required')
            return False
        return True
 
    def metametavar(self):
        tstr = re.sub(f',$','',re.sub(r'(\(|\)|class|\'|\s)','',repr(self.types)))
        return f'{tstr}'


class RangeValidator(Validator):
    def __init__(self, rmin, rmax, types=(float,)):
        if rmax < rmin:
            (rmin, rmax) = (rmax, rmin)
        self.rmin = rmin
        self.rmax = rmax
        self.types = types if isinstance(types,(list,tuple)) else (types,)

    def validate(self, x):
        if not isinstance(x,self.types):
            raise Exception(f'Argument is of type {type(x)}; but one of {repr(self.types)} required')
            return False
        if not (self.rmin <= x and x <= self.rmax):
            raise Exception(f'Argument is ({x}) not in range [{self.rmin},{self.rmax}]')
            return False
        return True

    def metametavar(self):
        tstr = re.sub(f',$','',re.sub(r'(\(|\)|class|\'|\s)','',repr(self.types)))
        return f'{tstr} in range [{self.rmin},{self.rmax}]'



class FunctionValidator(Validator):
    def __init__(self, func, types=(str,), message=''):
        self.func = func
        self.message = message
        self.types = types if isinstance(types,(list,tuple,)) else tuple([types])

    def validate(self, x):
        if not isinstance(x,self.types):
            raise Exception(f'Argument is of type {type(x)}; but one of {repr(self.types)} required')
            return False
      
        ok = self.func(x)
        if not ok:
            raise Exception(f'Argument {x} did not pass Func {repr(self.func)}')
            return False
        return True

    def metametavar(self):
        return self.message

if __name__ == '__main__':

    if False:
        w = OptionValidator(('x','y','z'))
        w.validate('x')
        print(w.metametavar())
        w.validate('a')

    if True:
        x = RangeValidator(-10,10,types=(int,float))
        x.validate(0)
        x.validate(10)
        print(x.metametavar())
        x.validate(11)
