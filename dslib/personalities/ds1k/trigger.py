from ... import validator
from . import common_validators

CONFIG = {
    'trigger': {
        'name': 'Trigger',
        'commands': {
            'trig_mode': {
                'base_str': ':TRIG:MODE',
                'validators': (
                    validator.OptionValidator(
                     ('edge','puls','runt','wind','nedg','slop','vid','patt','del',
                      'tim','dur','shol','rs232','iic','spi'),
                    ),
                ),
            },
            'trig_coupling': {
                'base_str': ':TRIG:COUP',
                'validators': (
                    validator.OptionValidator(('ac','dc','lfreject','hfreject')),
                ),
            },
            'trig_coupling': {
                'base_str': ':TRIG:SWE',
                'validators': (
                    validator.OptionValidator(('auto','normal','single')),
                ),
            },
            'trig_holdoff': {
                'base_str': ':TRIG:SWE',
                'validators': (
                    validator.RangeValidator(16e-9,10,(float,int)),
                ),
                'rtype': 'float',
            },
            'trig_noise_reject': {
                'base_str': ':TRIG:NREJ',
                'validators': (
                    common_validators.on_off,
                ),
            },
            'trig_source': {
                'base_str': ':TRIG:EDG:SOUR',
                'set_str': ':TRIG:EDG:SOUR {a0}',
                'validators': (
                    validator.OptionValidator(('chan1','chan2','chan3','chan4','ac')),
                ),
            },
            'trig_slope': {
                'base_str': ':TRIG:EDG:SLOP',
                'set_str': ':TRIG:EDG:SLOP {a0}',
                'validators': (
                    validator.OptionValidator(('positive','negative','rfali')),
                ),
            },
            'trig_level': {
                'base_str': ':TRIG:EDG:LEV',
                'validators': (
                    validator.TypeValidator((float,int)),
                ),
                'rtype': 'float',
            },
        }
    },
}
