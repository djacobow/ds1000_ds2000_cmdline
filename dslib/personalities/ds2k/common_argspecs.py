from ... import argspec

decoder_source = argspec.OptionArgSpec(
    ('d0','d1','d2','d3','d4','d5','d6','d6',
     'd8','d9','d10','d11','d12','d13','d14','d15',
     'chan1','chan2','off')
)

measure_source = argspec.OptionArgSpec(
    ('d0','d1','d2','d3','d4','d5','d6','d6',
     'd8','d9','d10','d11','d12','d13','d14','d15',
     'chan1','chan2','math')
)

decoder_number = argspec.OptionArgSpec((1,2), types=int)
channel_number = argspec.OptionArgSpec((1,2), types=int)
on_off         = argspec.OptionArgSpec((1,0,'1','0','on','off'), types=(str,int,))
is_percent     = argspec.RangeArgSpec(0,100,int)
cursor_pos_x   = argspec.RangeArgSpec(0,699,int)
cursor_pos_y   = argspec.RangeArgSpec(0,399,int)
neg_pos        = argspec.OptionArgSpec(('negative','positive'))
neg_pos_both   = argspec.OptionArgSpec(('negative','positive','both'))
ip_addr        = argspec.FunctionArgSpec(lambda x : re.match(r'^(\d+)\.(\d+)\.(\d+)\.(\d+)$',x), message='<ip_addr>')
high_low       = argspec.OptionArgSpec(('high','low'))
offset_pos     = argspec.RangeArgSpec(-166,148,int)
