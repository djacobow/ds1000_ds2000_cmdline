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
        image_dumper_group.add_argument(
            '--bw',
            action='store_true',
            help='Make a black and white image',
        )
        image_dumper_group.add_argument(
            '--invert',
            action='store_true',
            help='Invert the image colors',
        )
        image_dumper_group.add_argument(
            '--image-format', '-f',
            default='png',
            type=str,
            choices=('png','bmp8','bmp24','jpeg','tiff'),
            help='Invert the image colors',
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

        self.r.makeArgs(parser)
        return parser.parse_args()

    def go(self):
        res = self.r.dispatchArgs(self.args)
        print(json.dumps(res,indent=2))

        if self.args.capture is not None:
            fn = self.r.screenCap(
                self.args.capture,
                color = not self.args.bw,
                invert = self.args.invert,
                fmt = self.args.image_format
            )
            print(f'Wrote image: {fn}')

        if self.args.save_settings is not None:
            fn = self.r.saveSetup(self.args.save_settings)
            print(f'Wrote settings file: {fn}')
        elif self.args.load_settings is not None:
            fn = self.r.restoreSetup(self.args.load_settings)
            print(f'Restored settings from file: {fn}')

if __name__ == '__main__':

   if True:
       a = RigolCmdLine()
       a.go()

