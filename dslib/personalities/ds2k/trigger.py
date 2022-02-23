from ... import argspec
from . import common_argspecs

CONFIG = {
    'trigger': {
        'name': 'Trigger',
        'commands': {
            'trig_status': {
                'cmd': 'TRIGger:STATus?',
            },
            'trig_mode': {
                'base_str': ':TRIG:MODE',
                'argspecs': (
                    argspec.OptionArgSpec(
                        ('edge','pulse','runt','wind','nedge','slope','video','pattern',
                          'delay', 'timout','duration','shold','rs232','iic','spi','usb',
                          'can'),
                    ),
                ),
            },
            'trig_holdoff': {
                'base_str': ':TRIG:HOL',
                'argspecs': (
                    argspec.RangeArgSpec(100.0e-9,10,(float,int)),
                ),
            },
            'trig_coupling': {
                'base_str': ':TRIG:COUP',
                'argspecs': (
                    argspec.OptionArgSpec(('ac','dc','lfreject','hfreject')),
                ),
            },
            'trig_sweep': {
                'base_str': ':TRIG:SWE',
                'argspecs': (
                    argspec.OptionArgSpec(('auto','normal','single')),
                ),
            },
            'trig_noise_reject': {
                'base_str': ':TRIG:NREJ',
                'argspecs': (
                    common_argspecs.on_off,
                ),
            },
            'trig_source': {
                'base_str': ':TRIG:EDG:SOUR',
                'set_str': ':TRIG:EDG:SOUR {a0}',
                'argspecs': (
                    argspec.OptionArgSpec(('chan1','chan2','chan3','chan4','ac')),
                ),
            },
            'trig_slope': {
                'base_str': ':TRIG:EDG:SLOP',
                'set_str': ':TRIG:EDG:SLOP {a0}',
                'argspecs': (
                    argspec.OptionArgSpec(('positive','negative','rfali')),
                ),
            },
            'trig_level': {
                'base_str': ':TRIG:EDG:LEV',
                'argspecs': (
                    argspec.TypeArgSpec((float,int)),
                ),
                'rtype': 'float',
            },
        }
    },
}
