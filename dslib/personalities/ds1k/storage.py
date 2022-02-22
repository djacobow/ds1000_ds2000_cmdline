from ... import validator
from . import common_validators

CONFIG = {
    'storage': {
        'name': 'Image Storage Defaults',
        'simple_1_args': {
            'image_type': {
                'base_str': ':STOR:IMAG:TYPE',
                'validators': (
                    validator.OptionValidator(('png','bmp8','bmp24','jpeg','tiff')),
                ),
            },
            'image_invert': {
                'base_str': ':STOR:IMAG:INVERT',
                'validators': (
                    common_validators.on_off,
                ),
            },
            'image_color': {
                'base_str': ':STOR:IMAG:COLor',
                'validators': (
                    common_validators.on_off,
                ),
            },
        }
    }
}
