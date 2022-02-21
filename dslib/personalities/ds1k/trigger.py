CONFIG = {
    'trigger': {
        'name': 'Trigger',
        'simple_1_args': {
            'trig_mode': {
                'base_str': ':TRIG:MODE',
                'validators': (
                    ((str,),
                     ('edge','puls','runt','wind','nedg','slop','vid','patt','del',
                      'tim','dur','shol','rs232','iic','spi'),
                    ),
                ),
            },
            'trig_coupling': {
                'base_str': ':TRIG:COUP',
                'validators': (
                    ((str,), ('ac','dc','lfreject','hfreject')),
                ),
            },
            'trig_coupling': {
                'base_str': ':TRIG:SWE',
                'validators': (
                    ((str,), ('auto','normal','single')),
                ),
            },
            'trig_holdoff': {
                'base_str': ':TRIG:SWE',
                'validators': (
                    ((float,int), lambda x: 16e-9 < x and x < 10),
                ),
                'rtype': 'float',
            },
            'trig_noise_reject': {
                'base_str': ':TRIG:NREJ',
                'validators': (
                    ((str,int), (1,0,"on","off")),
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
