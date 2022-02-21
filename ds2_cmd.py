#!/usr/bin/env python3

import argparse
import json

import dslib

class RigolCmdLine(object):
    def __init__(self):
        self.r = dslib.RigolScope(personality='ds2k')
        self.args = self.parseArgs()
        self.r.connect(ip=self.args.host)

    def parseArgs(self):
        parser = argparse.ArgumentParser(description='Rigol DS10xxZ Command Line Tool')

        parser.add_argument(
            '--host','-ip',
            type=str,
            help='Unit\'s IP address',
            default='192.168.1.210'
        )
        image_dumper_group = parser.add_argument_group(
            title='Image Capture Options'
        )
        image_dumper_group.add_argument(
            '--capture','-c',
            nargs='?',
            type=str,
            default=None,
            const='',
            help='Name of image file to write'
        )

        sr_group = parser.add_argument_group(
            title="Saving and Restoring Complete Settings"
        )
        srme_group = sr_group.add_mutually_exclusive_group()
        srme_group.add_argument(
            '--save-settings','-d',
            nargs='?',
            type=str,
            default=None,
            const='',
            help='Name of settings file to write'
        )
        srme_group.add_argument(
            '--load-settings','-l',
            type=str,
            default=None,
            help='Name of settings file to load'
        )

        parser.add_argument(
            '--set-time','-t',
            action='store_true',
            help='Set the time on the scope to curent system time'
        )
        self.r.makeArgs(parser)
        return parser.parse_args()

    def go(self):
        res = self.r.dispatchArgs(self.args)
        print(json.dumps(res,indent=2))

        if self.args.capture is not None:
            fn = self.r.screenCap(
                self.args.capture,
                True, False, 'bmp'
            )
            print(f'Wrote image: {fn}')

        if self.args.save_settings is not None:
            fn = self.r.saveSetup(self.args.save_settings)
            print(f'Wrote settings file: {fn}')
        elif self.args.load_settings is not None:
            fn = self.r.restoreSetup(self.args.load_settings)
            print(f'Restored settings from file: {fn}')

        if self.args.set_time:
            self.r.setTime()

if __name__ == '__main__':

   if True:
       a = RigolCmdLine()
       a.go()

