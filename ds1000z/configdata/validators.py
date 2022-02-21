
decoder_source = (
    (str,),
    ('d0','d1','d2','d3','d4','d5','d6','d6',
     'd8','d9','d10','d11','d12','d13','d14','d15',
     'chan1','chan2','chan3','chan4','off')
)

measure_source = (
    (str,),
    ('d0','d1','d2','d3','d4','d5','d6','d6',
     'd8','d9','d10','d11','d12','d13','d14','d15',
     'chan1','chan2','chan3','chan4','math')
)

decoder_number = ((int,), (1,2))
channel_number = ((int,), (1,2,3,4))
on_off         = ((str,int), (1,0,'on','off'))
is_percent     = ((int,), lambda x : 0 <= x and x <= 100)
cursor_pos     = ((int,), lambda x : 5 <= x and x <= 594)
neg_pos        = ((str,), ('negative','positive'))
ip_addr        = ((str,), lambda x : re.match('^(\d+)\.(\d+)\.(\d+)\.(\d+)$',x))
