from ... import validator

decoder_source = validator.OptionValidator(
    ('d0','d1','d2','d3','d4','d5','d6','d6',
     'd8','d9','d10','d11','d12','d13','d14','d15',
     'chan1','chan2','off')
)

measure_source = validator.OptionValidator(
    ('d0','d1','d2','d3','d4','d5','d6','d6',
     'd8','d9','d10','d11','d12','d13','d14','d15',
     'chan1','chan2','math')
)

decoder_number = validator.OptionValidator((1,2), types=int)
channel_number = validator.OptionValidator((1,2), types=int)
on_off         = validator.OptionValidator((1,0,'1','0','on','off'), types=(str,int,))
is_percent     = validator.RangeValidator(0,100,int)
cursor_pos_x   = validator.RangeValidator(0,699,int)
cursor_pos_y   = validator.RangeValidator(0,399,int)
neg_pos        = validator.OptionValidator(('negative','positive'))
neg_pos_both   = validator.OptionValidator(('negative','positive','both'))
ip_addr        = validator.FunctionValidator(lambda x : re.match('^(\d+)\.(\d+)\.(\d+)\.(\d+)$',x), message='<ip_addr')
high_low       = validator.OptionValidator(('high','low'))
offset_pos     = validator.RangeValidator(-166,148,int)
