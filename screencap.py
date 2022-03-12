#!/usr/bin/env python3

import dslib
import datetime

if __name__ == '__main__':
   scope = dslib.RigolScope(ip='192.168.1.246')
   fname = f"capture_{datetime.datetime.now().isoformat()}.png"
   scope.capture(fname, 'color', 'normal', 'png')

