from ... import validator
from . import common_validators

CONFIG = {
    'acquire': {
        'name': 'Acquisition',
        'commands': {
            'sample_rate': {
                'cmd': ':ACQ:SRAT?',
            },
            'acq_average': {
                'base_str': ':ACQ:AVER',
                'validators': (
                    validator.RangeValidator(1,13,int),
                ),
                'rtype': 'int',
            },
            'acq_depth': {
                'base_str': ':ACQ:MDEPTH',
                'validators': (
                    validator.OptionValidator(
                     ('auto','14000','140000','1400000', '14000000', '56000000',
                      '7000','70000','700000','7000000','28000000'),
                    ),
                ),
            },
            'acq_type': {
                'base_str': ':ACQ:TYPE',
                'validators': (
                    validator.OptionValidator(('normal','averages','peak','hresolution')),
                ),
            },
            'acq_antialias': {
                'base_str': ':ACQ:AALI',
                'validators': (
                    common_validators.on_off,
                ),
            },
        },
    },
}
