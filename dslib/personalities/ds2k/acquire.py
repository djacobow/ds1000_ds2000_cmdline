from . import validators

CONFIG = {
    'acquire': {
        'name': 'Acquisition',
        'simple_0_args': {
            'sample_rate': {
                'cmd': ':ACQ:SRAT?',
            },
        },
        'simple_1_args': {
            'acq_average': {
                'base_str': ':ACQ:AVER',
                'validators': (
                    ((int,), lambda x: x <= 1 and x <= 13),
                ),
                'rtype': 'int',
            },
            'acq_depth': {
                'base_str': ':ACQ:MDEPTH',
                'validators': (
                    ((str,),
                     ('auto','14000','140000','1400000', '14000000', '56000000',
                      '7000','70000','700000','7000000','28000000'),
                    ),
                ),
            },
            'acq_type': {
                'base_str': ':ACQ:TYPE',
                'validators': (
                    ((str,), ('normal','averages','peak','hresolution')),
                ),
            },
            'acq_antialias': {
                'base_str': ':ACQ:AALI',
                'validators': (
                    validators.on_off,
                ),
            },
        },
    },
}
