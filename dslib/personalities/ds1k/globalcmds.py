from ... import validator

CONFIG = {
    'global': {
        'name': 'Global',
        'commands': {
            'id': {
                'help': 'Get the instrument ID including serial number',
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
                'help': 'equivalent to hitting the "auto" button on the unit',
                'cmd': ':AUTOscale',
            },
            'clear': {
                'cmd': ':CLEar',
            },
            'run': {
                'help': 'set sweep to run',
                'cmd': ':RUN',
            },
            'stop': {
                'help': 'set sweep to stop',
                'cmd': ':STOP',
            },
            'single': {
                'help': 'set sweep once on trigger',
                'cmd': ':SINGle',
            },
            'force_trigger': {
                'help': 'force trigger immediately',
                'cmd': ':TFORce',
            },
            'trig_status': {
                'help': 'return trigger status',
                'cmd': ':TRIG:STAT?',
            },
            'trig_position': {
                'help': 'report trigger position',
                'cmd': ':TRIG:POS?',
            },
            'sample_rate': {
                'help': 'report sample rate',
                'cmd': ':ACQ:SRAT?',
            },
            'calibrate': {
                'help': 'report sample rate',
                'cmd': ':CALIbrate:START',
            },
            'calibrate_quit': {
                'help': 'start calibration routine',
                'cmd': ':CALIbrate:QUIT',
            },
            'cursor_mode': {
                'help': 'get/set cursor mode',
                'base_str': ':CURSor:MODE',
                'validators': (
                    validator.OptionValidator(('off','manual','track','auto','xy')),
                ),
            },
        },
    }
}
