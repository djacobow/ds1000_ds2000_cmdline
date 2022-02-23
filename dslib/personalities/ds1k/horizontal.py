from ... import argspec
from . import common_argspecs

CONFIG = {
    'horizontal': {
        'name': 'Horizontal',
        'commands': {
            'horiz_delay': {
                'base_str': ':TIM:DEL:ENAB',
                'argspecs': (
                    common_argspecs.on_off,
                ),
            },
            'horiz_delay_offset': {
                'base_str': ':TIM:DEL:OFFS',
                'argspecs': (
                    argspec.TypeArgSpec((float,int)),
                ),
            },
            'horiz_offset': {
                'base_str': ':TIM:MAIN:OFFS',
                'argspecs': (
                    argspec.TypeArgSpec((float,int)),
                ),
            },
            'horiz_mode': {
                'base_str': ':TIM:MODE',
                'argspecs': (
                    argspec.OptionArgSpec(('main','xy','roll')),
                ),
            },
            'horiz_scale': {
                'base_str': ':TIMebase:MAIN:SCALe',
                'argspecs': (
                    argspec.OptionArgSpec(
                        (
                            5e-9,
                            1e-8, 2e-8, 5e-8,
                            1e-7, 2e-7, 5e-7,
                            1e-6, 2e-6, 5e-6,
                            1e-5, 2e-5, 5e-5,
                            1e-4, 2e-4, 5e-4,
                            1e-3, 2e-3, 5e-3,
                            1e-2, 2e-2, 5e-2,
                            1e-1, 2e-1, 5e-1,
                            1, 2, 5,
                            10, 20, 50,
                        ),
                        (float, int)
                    ),
                ),
                'rtype': 'float',
            },
        }
    },
}

