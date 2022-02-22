from ... import validator
from . import common_validators

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
                    common_validators.on_off,
                ),
            },
            'sys_enable_beep': {
                'base_str': ':SYST:BEEP',
                'validators': (
                    common_validators.on_off,
                ),
            },
            'sys_lock_keyboard': {
                'base_str': ':SYST:LOCK',
                'validators': (
                    validator.OptionValidator(('latest','default')),
                ),
            },
            'sys_poweron_config': {
                'base_str': ':SYST:PON',
                'validators': (
                    common_validators.on_off,
                ),
            },
            'sys_option_install': {
                'base_str': ':SYST:OPT:INST',
                'validators': (
                    validator.TypeValidator(str),
                ),
            },
            'sys_language': {
                'base_str': ':SYST:LANG',
                'validators': (
                    validator.OptionValidator(
                        ('schinese','tchinese','english','portuguese',
                         'german','polish','korean','japanese','french',
                         'russian'
                        )
                    ),
                ),
            },
        }
    }
}
