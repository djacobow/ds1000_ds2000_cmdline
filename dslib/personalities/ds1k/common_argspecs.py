from ... import argspec

decoder_source = argspec.OptionArgSpec(
    ('d0','d1','d2','d3','d4','d5','d6','d6',
     'd8','d9','d10','d11','d12','d13','d14','d15',
     'chan1','chan2','chan3','chan4','off')
)

measure_source = argspec.OptionArgSpec(
    ('d0','d1','d2','d3','d4','d5','d6','d6',
     'd8','d9','d10','d11','d12','d13','d14','d15',
     'chan1','chan2','chan3','chan4','math')
)

decoder_number = argspec.OptionArgSpec((1,2), types=int)
channel_number = argspec.OptionArgSpec((1,2,3,4), types=int)
on_off         = argspec.OptionArgSpec(('1','0',1,0,'on','off'), types=(str,int,))
is_percent     = argspec.RangeArgSpec(0,100,int)
cursor_pos     = argspec.RangeArgSpec(5, 594,int)
neg_pos        = argspec.OptionArgSpec(('negative','positive'))
ip_addr        = argspec.FunctionArgSpec(lambda x: re.match('^(\d+)\.(\d+)\.(\d+)\.(\d+)$',x), message='<ip_addr>')

