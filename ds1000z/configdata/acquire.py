CONFIG = {
    'acquire': {
        'name': 'Acquisition',
        'simple_1_args': {
            'acq_average': {
                'base_str': ':ACQ:AVER',
                'validators': (
                    ((int,), None),
                ),
                'rtype': 'int',
            },
            'acq_depth': {
                'base_str': ':ACQ:MDEPTH',
                'validators': (
                    ((int,), None),
                ),
                'rtype': 'int',
            },
            'acq_type': {
                'base_str': ':ACQ:TYPE',
                'validators': (
                    ((str,), ('normal','averages','peak','hresolution')),
                ),
            },
        },
    },
}
