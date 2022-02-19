#!/usr/bin/env python3

import argparse
import json

import ds1000z

class RigolCmdLine(object):
    def __init__(self):
        self.r = ds1000z.RigolDS1000z()
        self.args = self.parseArgs()
        # print(self.args)
        self.r.connect(ip=self.args.host)

    def parseArgs(self):
        parser = argparse.ArgumentParser(description='Rigol DS10xxZ Command Line Tool')

        parser.add_argument(
            '--host','-ip',
            type=str,
            help='Unit\'s IP address',
            default='192.168.1.246'
        )
        parser.add_argument(
            '--capture','-c',
            nargs='?',
            type=str,
            default=None,
            const='',
            help='Name of image file to write'
        )

        self.r.makeArgs(parser)
        return parser.parse_args()

    def go(self):
        res = self.r.dispatchArgs(self.args)
        print(json.dumps(res,indent=2))

        if self.args.capture is not None:
            fn = self.r.screenCap(self.args.capture)
            print(f'Wrote image: {fn}')

if __name__ == '__main__':

   if True:
       a = RigolCmdLine()
       a.go()

