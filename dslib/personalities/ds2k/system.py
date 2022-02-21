from . import validators

CONFIG = {
    'system': {
        'name': 'System Commands',
        'simple_0_args': {
            'sys_last_error': {
                'cmd': ':SYST:ERR?',
            },
            'sys_horiz_grid_count': {
                'cmd': ':SYST:GAM?',
            },
            'sys_ram': {
                'cmd': ':SYST:RAM?',
            },
            'sys_options_valid': {
                'cmd': ':SYST:OPT:VALid?',
            },
            'sys_reset': {
                'cmd': ':SYST:RESet',
            },
            'sys_gettime': {
                'cmd': ':SYST:TIME?',
            },
            'sys_version': {
                'cmd': ':SYST:VERSion?',
            },
        },
        'simple_1_args': {
            'sys_trig_out': {
                'base_str': ':SYST:AOUT',
                'validators': (
                    ((str,), ('tout','pfail')),
                ),
            },
            'sys_enable_autoscale': {
                'base_str': ':SYST:AUT',
                'validators': (
                    validators.on_off,
                ),
            },
            'sys_enable_beep': {
                'base_str': ':SYST:BEEP',
                'validators': (
                    validators.on_off,
                ),
            },
            'sys_expand_reference': {
                'base_str': ':SYST:EXP',
                'validators': (
                    ((str,), ('center','ground')),
                ),
            },
            'sys_gpip_addr': {
                'base_str': ':SYST:GPIB',
                'validators': (
                    ((int,), lambda x: 1 <= x and x <= 30),
                ),
            },
            'sys_keypress': {
                'base_str': ':SYST:KEY:PRES',
                'validators': (
                    ((str,),
                    ('ch1','ch2','math','ref','la','decode1','decode2','aoff',
                     'moff','f1','f2','f3','f4','f5','f6','f7','qprevious','qnext',
                     'vposition','vposition1','vposition2','vscale','vscale1',
                     'vscale2','hscale','hposition','hmenu','kfunction','tlevel',
                     'tmenu','tforce','tmode','clear','auto','rstop','single',
                     'qprint','measure','acquire','storage','cursor','display',
                     'utility','help','srecord','erecord','ppause',
                     'ffp10','ffp20','ffp30','ffp40','ffp50','ffp60','ffp70',
                     'ffn10','ffn20','ffn30','ffn40','ffn50','ffn60','ffn70',
                     'source'
                    )),
                ),
            },
            'sys_key_increase': {
                'base_str': ':SYST:KEY:INCR',
                'validators': (
                    ((int,), None),
                ),
            },
            'sys_key_decrease': {
                'base_str': ':SYST:KEY:DECR',
                'validators': (
                    ((int,), None),
                ),
            },
            'sys_poweron_config': {
                'base_str': ':SYST:PON',
                'validators': (
                    validators.on_off,
                ),
            },
            'sys_power_on_status': {
                'base_str': ':SYST:PSTATUS',
                'validators': (
                    ((str,), ('default','open')),
                ),
            },
            'sys_option_install': {
                'base_str': ':SYST:OPT:INST',
                'validators': (
                    ((str,), None),
                ),
            },
            'sys_language': {
                'base_str': ':SYST:LANG',
                'validators': (
                    ((str,),
                    ('schinese','tchinese','english','portuguese',
                     'german','polish','korean','japanese','french',
                     'russian'
                    )),
                ),
            },
            'sys_screensaver_timer': {
                'base_str': ':SYST:SSAV:TIME',
                'validators': (
                    ((str,), ('1min','2min','5min','15min','30min',
                              '45min','60min','2hour','5hour','off')),
                ),
            },
            'sys_usb_device_mode': {
                'base_str': ':SYST:UDEV',
                'validators': (
                    ((str,), ('computer','pictbridge')),
                ),
            },
        }
    }
}
