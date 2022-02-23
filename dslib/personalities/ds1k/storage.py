from ... import argspec
from . import common_argspecs

CONFIG = {
    'storage': {
        'name': 'Image Storage Defaults',
        'commands': {
            'image_type': {
                'base_str': ':STOR:IMAG:TYPE',
                'argspecs': (
                    argspec.OptionArgSpec(('png','bmp8','bmp24','jpeg','tiff')),
                ),
            },
            'image_invert': {
                'base_str': ':STOR:IMAG:INVERT',
                'argspecs': (
                    common_argspecs.on_off,
                ),
            },
            'image_color': {
                'base_str': ':STOR:IMAG:COLor',
                'argspecs': (
                    common_argspecs.on_off,
                ),
            },
        }
    }
}
