from ... import validator
from . import common_validators

CONFIG = {
    'display': {
        'name': 'Display',
        'simple_0_args': {
            'disp_clear': {
                'cmd': ':DISP:CLEar',
            }
        },
        'simple_1_args': {
            'disp_type': {
                'base_str': ':DISP:TYPE',
                'validators': (
                    validator.OptionValidator(('vectors','dots')),
                ),
            },
            'disp_grading_time': {
                'base_str': ':DISP:GRAD:TIME',
                'validators': (
                    validator.OptionValidator(('min','inf','infinite',0.05,0.1,0.2,0.5,1,5,10,20),(str,float,int)),
                ),
            },
            'disp_wave_brightness': {
                'base_str': ':DISP:WBR',
                'validators': (
                    common_validators.is_percent,
                ),
            },
            'disp_grid_brightness': {
                'base_str': ':DISP:GBR',
                'validators': (
                    common_validators.is_percent,
                ),
            },
            'disp_menu_time': {
                'base_str': ':DISP:MPER',
                'validators': (
                    validator.OptionValidator((1,2,5,10,20,'infinite'),(str,float,int)),
                ),
            },
            'disp_grid': {
                'base_str': ':DISP:GRID',
                'validators': (
                    validator.OptionValidator(('full','half','none')),
                ),
            },
        },
    },
}

