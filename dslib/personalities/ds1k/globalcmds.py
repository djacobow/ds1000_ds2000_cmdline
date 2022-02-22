from ... import validator

CONFIG = {
    'global': {
        'name': 'Global',
        'simple_0_args': {
            'id': {
                'cmd': '*IDN?',
            },
            'event_status': {
                'cmd': '*ESR?',
            },
            'reset': {
                'cmd': '*RST',
            },
            'self_test': {
                'cmd': '*TST?',
            },
            'wait': {
                'cmd': '*WAI',
            },
            'auto': {
                'cmd': ':AUTOscale',
            },
            'clear': {
                'cmd': ':CLEar',
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
            'trig_status': {
                'cmd': ':TRIG:STAT?',
            },
            'trig_position': {
                'cmd': ':TRIG:POS?',
            },
            'sample_rate': {
                'cmd': ':ACQ:SRAT?',
            },
            'calibrate': {
                'cmd': ':CALIbrate:START',
            },
            'calibrate_quit': {
                'cmd': ':CALIbrate:QUIT',
            },
        },
        'simple_1_args': {
            'cursor_mode': {
                'base_str': ':CURSor:MODE',
                'validators': (
                    validator.OptionValidator(('off','manual','track','auto','xy')),
                ),
            },
        },
    }
}
