from ... import validator
from . import common_validators

CONFIG = {
    'channel': {
        'name': 'Channel',
        'commands': {
            'ch_scale': {
                'q_str':   ':CHAN{a0}:SCAL?',
                'set_str': ':CHAN{a0}:SCAL {a1}',
                'validators': (
                    common_validators.channel_number,
                    validator.OptionValidator((0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100),(float,int)),
                ),
                'rtype': 'float',
            },
            'ch_probe': {
                'q_str': ':CHAN{a0}:PROB?',
                'set_str': ':CHAN{a0}:PROB {a1}',
                'validators': (
                    common_validators.channel_number,
                    validator.OptionValidator((0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 500, 1000),(float,int)),
                ),
                'rtype': 'float',
            },
            'ch_display': {
                'q_str': ':CHAN{a0}:DISP?',
                'set_str': ':CHAN{a0}:DISP {a1}',
                'validators': (
                    common_validators.channel_number,
                    common_validators.on_off,
                ),
            },
            'ch_units': {
                'q_str': ':CHAN{a0}:UNITs?',
                'set_str': ':CHAN{a0}:UNITs {a1}',
                'validators': (
                    common_validators.channel_number,
                    validator.OptionValidator(('voltage','watt','ampere','unknown')),
                ),
            },
            'ch_bwlimit': {
                'q_str': ':CHAN{a0}:BWL?',
                'set_str': ':CHAN{a0}:BWL {a1}',
                'validators': (
                    common_validators.channel_number,
                    validator.OptionValidator(('20m','off')),
                ),
            },
            'ch_coupling': {
                'q_str': ':CHAN{a0}:COUP?',
                'set_str': ':CHAN{a0}:COUP {a1}',
                'validators': (
                    common_validators.channel_number,
                    validator.OptionValidator(('ac','dc','gnd')),
               ),
            },
            'ch_invert': {
                'q_str': ':CHAN{a0}:INV?',
                'set_str': ':CHAN{a0}:INV {a1}',
                'validators': (
                    common_validators.channel_number,
                    common_validators.on_off,
                ),
                'rtype': 'int',
            },
            'ch_impedance': {
                'q_str': ':CHAN{a0}:IMP?',
                'set_str': ':CHAN{a0}:IMP {a1}',
                'validators': (
                    common_validators.channel_number,
                    validator.OptionValidator(('omeg','fifty')),
                ),
            },
            'ch_vernier': {
                'q_str': ':CHAN{a0}:VERN?',
                'set_str': ':CHAN{a0}:VERN {a1}',
                'validators': (
                    common_validators.channel_number,
                    common_validators.on_off,
                ),
                'rtype': 'int',
            },
            'ch_delay_calibration': {
                'q_str': ':CHAN{a0}:TCAL?',
                'set_str': ':CHAN{a0}:TCAL {a1}',
                'validators': (
                    common_validators.channel_number,
                    validator.RangeValidator(-200e-9, 200e-9, float),
                    common_validators.on_off,
                ),
                'rtype': 'int',
            },
            'ch_offset': {
                'q_str': ':CHANnel{a0}:OFFSet?',
                'set_str': ':CHANnel{a0}:OFFSet {a1}',
                'validators': (
                    common_validators.channel_number,
                    validator.TypeValidator(float),
                ),
                'rtype': 'float',
            },
        },
    },
}

