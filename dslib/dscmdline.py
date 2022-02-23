#!/usr/bin/env python3

import argparse
import json
import os
import textwrap as _textwrap

import dslib

class RigolCmdLine(object):
    def __init__(self, personality='ds1k'):
        self.personality = personality
        self.r = dslib.RigolScope(personality=personality)
        self.args = self.parseArgs()
        self.r.connect(ip=self.args.host)

    def parseArgs(self):
        parser = argparse.ArgumentParser(
            description=f'Rigol {self.personality} Command Line Tool',
        )

        parser.add_argument(
            '--host','-ip',
            type=str,
            help='Unit\'s IP address',
            default='192.168.1.246' if self.personality == 'ds1k' else '192.168.1.210',
        )

        self.r.addArgs(parser)
        args = parser.parse_args()
        # print(json.dumps(vars(args),indent=2))
        return args

    def go(self):
        res = self.r.dispatchArgs(self.args)
        print(json.dumps(res,indent=2))

if __name__ == '__main__':
    pass
