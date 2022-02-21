from . import validators

CONFIG = {
    'storage': {
        'name': 'Image Storage Defaults',
        'simple_1_args': {
            'image_type': {
                'base_str': ':STOR:IMAG:TYPE',
                'validators': (
                    ((str,), ('png','bmp8','bmp24','jpeg','tiff')),
                ),
            },
            'image_invert': {
                'base_str': ':STOR:IMAG:INVERT',
                'validators': (
                    validators.on_off,
                ),
            },
            'image_color': {
                'base_str': ':STOR:IMAG:COLor',
                'validators': (
                    validators.on_off,
                ),
            },
        }
    }
}
