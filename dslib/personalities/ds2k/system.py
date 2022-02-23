from ... import argspec
from . import common_argspecs

def setTime(rs, args):
    now = datetime.datetime.now()
    hours = now.hour
    minutes = now.minute
    seconds = now.second
    rs._cmd0(f':SYST:TIME {hours},{minutes},{seconds}')

def storeSetup(rs, args):
    rs.saveSetup(args[0] if len(args) else None)

def loadSetup(rs, args):
    rs.restoreSetup(args[0])


CONFIG = {
    'system': {
        'name': 'System Commands',
        'commands': {
            'sys_settime': {
                'func': setTime,
                'argspecs': (),
            },
            'sys_store_setup': {
                'func': storeSetup,
                'argspecs': (
                   argspec.TypeArgSpec((str,None)),
                ),
            },
            'sys_save_setup': {
                'func': loadSetup,
                'argspecs': (
                   argspec.TypeArgSpec(str),
                ),
            },
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
            'sys_trig_out': {
                'base_str': ':SYST:AOUT',
                'argspecs': (
                    argspec.OptionArgSpec(('tout','pfail')),
                ),
            },
            'sys_enable_autoscale': {
                'base_str': ':SYST:AUT',
                'argspecs': (
                    common_argspecs.on_off,
                ),
            },
            'sys_enable_beep': {
                'base_str': ':SYST:BEEP',
                'argspecs': (
                    common_argspecs.on_off,
                ),
            },
            'sys_expand_reference': {
                'base_str': ':SYST:EXP',
                'argspecs': (
                    argspec.OptionArgSpec(('center','ground')),
                ),
            },
            'sys_gpip_addr': {
                'base_str': ':SYST:GPIB',
                'argspecs': (
                    argspec.RangeArgSpec(1,30,int),
                ),
            },
            'sys_keypress': {
                'base_str': ':SYST:KEY:PRES',
                'argspecs': (
                    argspec.OptionArgSpec(
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
                'argspecs': (
                    argspec.TypeArgSpec(int),
                ),
            },
            'sys_key_decrease': {
                'base_str': ':SYST:KEY:DECR',
                'argspecs': (
                    argspec.TypeArgSpec(int),
                ),
            },
            'sys_poweron_config': {
                'base_str': ':SYST:PON',
                'argspecs': (
                    common_argspecs.on_off,
                ),
            },
            'sys_power_on_status': {
                'base_str': ':SYST:PSTATUS',
                'argspecs': (
                    argspec.OptionArgSpec(('default','open')),
                ),
            },
            'sys_option_install': {
                'base_str': ':SYST:OPT:INST',
                'argspecs': (
                    argspec.TypeArgSpec(str),
                ),
            },
            'sys_language': {
                'base_str': ':SYST:LANG',
                'argspecs': (
                    argspec.OptionArgSpec( 
                     ('schinese','tchinese','english','portuguese',
                     'german','polish','korean','japanese','french',
                     'russian'
                    )),
                ),
            },
            'sys_screensaver_timer': {
                'base_str': ':SYST:SSAV:TIME',
                'argspecs': (
                    argspec.OptionArgSpec(
                        ('1min','2min','5min','15min','30min',
                         '45min','60min','2hour','5hour','off')
                    ),
                ),
            },
            'sys_usb_device_mode': {
                'base_str': ':SYST:UDEV',
                'argspecs': (
                    argspec.OptionArgSpec(('computer','pictbridge')),
                ),
            },
        }
    }
}
