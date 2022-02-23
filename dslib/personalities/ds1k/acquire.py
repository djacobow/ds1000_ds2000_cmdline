from ... import validator

CONFIG = {
    'acquire': {
        'name': 'Acquisition',
        'commands': {
            'acq_average': {
                'base_str': ':ACQ:AVER',
                'validators': (
                    validator.TypeValidator(int),
                ),
                'rtype': 'int',
            },
            'acq_depth': {
                'base_str': ':ACQ:MDEPTH',
                'validators': (
                    validator.TypeValidator(int),
                ),
                'rtype': 'int',
            },
            'acq_type': {
                'base_str': ':ACQ:TYPE',
                'validators': (
                    validator.TypeValidator(int),
                ),
            },
        },
    },
}
