from ... import argspec

CONFIG = {
    'acquire': {
        'name': 'Acquisition',
        'commands': {
            'acq_average': {
                'base_str': ':ACQ:AVER',
                'argspecs': (
                    argspec.TypeArgSpec(int),
                ),
                'rtype': 'int',
            },
            'acq_depth': {
                'base_str': ':ACQ:MDEPTH',
                'argspecs': (
                    argspec.TypeArgSpec(int),
                ),
                'rtype': 'int',
            },
            'acq_type': {
                'base_str': ':ACQ:TYPE',
                'argspecs': (
                    argspec.TypeArgSpec(int),
                ),
            },
        },
    },
}
