from ... import validator

CONFIG = {
    'global': {
        'name': 'Global',
        'simple_0_args': {
            'auto': {
                'cmd': ':AUTOscale',
            },
            'run': {
                'cmd': ':RUN',
            },
            'stop': {
                'cmd': ':STOP',
            },
            'single': {
                'cmd': ':SINGle',
            },
            'force_trigger': {
                'cmd': ':TFORce',
            },
            'trig_level_half': {
                'cmd': ':TLHA',
            },
            'clear_event_registers': {
                'cmd': ':*CLS',
            },
            'event_status': {
                'cmd': '*ESR?',
            },
            'id': {
                'cmd': '*IDN?',
            },
            'reset': {
                'cmd': '*RST',
            },
            'read_state_register': {
                'cmd': '*STB?',
            },
            'self_test': {
                'cmd': '*TST?',
            },
        },
        'simple_1_args': {
            'event_register_mask': {
                'base_str': ':*ESE',
                'validators': (
                    validator.RangeValidator(0,255,int),
                ),
            },
            'enable_register_state': {
                'base_str': ':*SRE',
                'validators': (
                    validator.RangeValidator(0,255,int),
                ),
            },
        },
    }
}
