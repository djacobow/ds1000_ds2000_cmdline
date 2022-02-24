#!/usr/bin/env python3

CONFIG = {
    'subpaths': {
        'l':   ( 'dslib',          ['dslib']),
        'ps':  ( 'personaliities', ['dslib','personalities']),
        'd1':  ( 'ds1k',           ['dslib','personalities','ds1k']),
        'd2':  ( 'ds2k',           ['dslib','personalities','ds2k']),
    },
    'code_file_types': {
        'py':    { 'default': True,  },
    },
    'code_search_paths': {
        'ds1000_ds2000_cmdline': {
            'dslib': {
                'default': True,
                'include': ['dslib'],
                'exclude': r'personalities',
            },
            'ds1k': {
                'default': True,
                'include': ['dslib/personalities/ds1k'],
            },
            'ds2k': {
                'default': True,
                'include': ['dslib/personalities/ds2k'],
            },
        },
    },
    'commands': {
    }
}

