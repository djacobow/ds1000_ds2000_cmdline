from . import validators

CONFIG = {
    'system': {
        'name': 'System Commands',
        'simple_0_args': {
            'sys_last_error': {
                'cmd': ':SYST:ERR?',
            },
            'sys_horiz_grid_count': {
                'cmd': ':SYST:GAM?',
            },
            'sys_ram': {
                'cmd': ':SYST:RAM?',
            },
        },
        'simple_1_args': {
            'sys_enable_autoscale': {
                'base_str': ':SYST:AUT',
                'validators': (
                    validators.on_off,
                ),
            },
            'sys_enable_beep': {
                'base_str': ':SYST:BEEP',
                'validators': (
                    validators.on_off,
                ),
            },
            'sys_lock_keyboard': {
                'base_str': ':SYST:LOCK',
                'validators': (
                    ((str,), ('latest','default')),
                ),
            },
            'sys_poweron_config': {
                'base_str': ':SYST:PON',
                'validators': (
                    validators.on_off,
                ),
            },
            'sys_option_install': {
                'base_str': ':SYST:OPT:INST',
                'validators': (
                    ((str,), None),
                ),
            },
            'sys_language': {
                'base_str': ':SYST:LANG',
                'validators': (
                    ((str,),
                    ('schinese','tchinese','english','portuguese',
                     'german','polish','korean','japanese','french',
                     'russian'
                    )),
                ),
            },
        }
    }
}
