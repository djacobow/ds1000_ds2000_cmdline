from ... import argspec

CONFIG = {
    'global': {
        'name': 'Global',
        'commands': {
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
        'commands': {
            'event_register_mask': {
                'base_str': ':*ESE',
                'argspecs': (
                    argspec.RangeArgSpec(0,255,int),
                ),
            },
            'enable_register_state': {
                'base_str': ':*SRE',
                'argspecs': (
                    argspec.RangeArgSpec(0,255,int),
                ),
            },
        },
    }
}
