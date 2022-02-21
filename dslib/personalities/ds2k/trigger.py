from . import validators

CONFIG = {
    'trigger': {
        'name': 'Trigger',
        'simple_0_args': {
            'trig_status': {
                'cmd': 'TRIGger:STATus?',
            },
        },
        'simple_1_args': {
            'trig_mode': {
                'base_str': ':TRIG:MODE',
                'validators': (
                    ((str,),
                     ('edge','pulse','runt','wind','nedge','slope','video','pattern',
                      'delay', 'timout','duration','shold','rs232','iic','spi','usb',
                      'can'),
                    ),
                ),
            },
            'trig_holdoff': {
                'base_str': ':TRIG:HOL',
                'validators': (
                    ((float,int), lambda x: 100.0e-9 <= x and x <= 10),
                ),
            },
            'trig_coupling': {
                'base_str': ':TRIG:COUP',
                'validators': (
                    ((str,), ('ac','dc','lfreject','hfreject')),
                ),
            },
            'trig_sweep': {
                'base_str': ':TRIG:SWE',
                'validators': (
                    ((str,), ('auto','normal','single')),
                ),
            },
            'trig_noise_reject': {
                'base_str': ':TRIG:NREJ',
                'validators': (
                    validators.on_off,
                ),
            },
            'trig_source': {
                'base_str': ':TRIG:EDG:SOUR',
                'set_str': ':TRIG:EDG:SOUR {a0}',
                'validators': (
                    ((str), ('chan1','chan2','chan3','chan4','ac')),
                ),
            },
            'trig_slope': {
                'base_str': ':TRIG:EDG:SLOP',
                'set_str': ':TRIG:EDG:SLOP {a0}',
                'validators': (
                    ((str), ('positive','negative','rfali')),
                ),
            },
            'trig_level': {
                'base_str': ':TRIG:EDG:LEV',
                'validators': (
                    ((float,int), None),
                ),
                'rtype': 'float',
            },
        }
    },
}
