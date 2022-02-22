from ... import validator
from . import common_validators

CONFIG = {
    'channel': {
        'name': 'Channel',
        'simple_2_args': {
            'ch_scale': {
                'help': 'Get/Set the channel gain',
                'q_str':   ':CHAN{a0}:SCAL?',
                'set_str': ':CHAN{a0}:SCAL {a1}',
                'validators': (
                    common_validators.channel_number,
                    validator.OptionValidator((0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100),(float,int)),
                ),
                'rtype': 'float',
            },
            'ch_probe': {
                'help': 'Get/Set the probe attenuation displayed',
                'q_str': ':CHAN{a0}:PROB?',
                'set_str': ':CHAN{a0}:PROB {a1}',
                'validators': (
                    common_validators.channel_number,
                    validator.OptionValidator((0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100),(float,int)),
                ),
                'rtype': 'float',
            },
            'ch_display': {
                'help': 'Get/Set channel display status',
                'q_str': ':CHAN{a0}:DISP?',
                'set_str': ':CHAN{a0}:DISP {a1}',
                'validators': (
                    common_validators.channel_number,
                    common_validators.on_off,
                ),
            },
            'ch_bwlimit': {
                'help': 'Apply bw limiting to channel',
                'q_str': ':CHAN{a0}:BWL?',
                'set_str': ':CHAN{a0}:BWL {a1}',
                'validators': (
                    common_validators.channel_number,
                    validator.OptionValidator(('20m','off')),
                ),
            },
            'ch_coupling': {
                'help': 'Get/set the channel coupling mode',
                'q_str': ':CHAN{a0}:COUP?',
                'set_str': ':CHAN{a0}:COUP {a1}',
                'validators': (
                    common_validators.channel_number,
                    validator.OptionValidator(('ac','dc','gnd')),
               ),
            },
            'ch_invert': {
                'help': 'Get/set the channel inversion mode',
                'q_str': ':CHAN{a0}:INV?',
                'set_str': ':CHAN{a0}:INV {a1}',
                'validators': (
                    common_validators.channel_number,
                    common_validators.on_off,
                ),
                'rtype': 'int',
            },
            'ch_vernier': {
                'help': 'Get/set vernier mode for channel gain',
                'q_str': ':CHAN{a0}:VERN?',
                'set_str': ':CHAN{a0}:VERN {a1}',
                'validators': (
                    common_validators.channel_number,
                    common_validators.on_off,
                ),
                'rtype': 'int',
            },
            'ch_offset': {
                'help': 'Get/set channel vertical offset',
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

