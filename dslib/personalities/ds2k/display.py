from . import validators

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
                    ((str,),('vectors','dots')),
                ),
            },
            'disp_grading_time': {
                'base_str': ':DISP:GRAD:TIME',
                'validators': (
                    ((str,float,int), ('min','inf','infinite',0.05,0.1,0.2,0.5,1,5,10,20)),
                ),
            },
            'disp_wave_brightness': {
                'base_str': ':DISP:WBR',
                'validators': (
                    validators.is_percent,
                ),
            },
            'disp_grid_brightness': {
                'base_str': ':DISP:GBR',
                'validators': (
                    validators.is_percent,
                ),
            },
            'disp_menu_time': {
                'base_str': ':DISP:MPER',
                'validators': (
                    ((str,float,int), (1,2,5,10,20,'infinite')),
                ),
            },
            'disp_grid': {
                'base_str': ':DISP:GRID',
                'validators': (
                    ((str,), ('full','half','none')),
                ),
            },
        },
    },
}

