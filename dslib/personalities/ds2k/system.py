from ... import validator
from . import common_validators

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
                'validators': (),
            },
            'sys_store_setup': {
                'func': storeSetup,
                'validators': (
                   validator.TypeValidator((str,None)),
                ),
            },
            'sys_save_setup': {
                'func': loadSetup,
                'validators': (
                   validator.TypeValidator(str),
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
                'validators': (
                    validator.OptionValidator(('tout','pfail')),
                ),
            },
            'sys_enable_autoscale': {
                'base_str': ':SYST:AUT',
                'validators': (
                    common_validators.on_off,
                ),
            },
            'sys_enable_beep': {
                'base_str': ':SYST:BEEP',
                'validators': (
                    common_validators.on_off,
                ),
            },
            'sys_expand_reference': {
                'base_str': ':SYST:EXP',
                'validators': (
                    validator.OptionValidator(('center','ground')),
                ),
            },
            'sys_gpip_addr': {
                'base_str': ':SYST:GPIB',
                'validators': (
                    validator.RangeValidator(1,30,int),
                ),
            },
            'sys_keypress': {
                'base_str': ':SYST:KEY:PRES',
                'validators': (
                    validator.OptionValidator(
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
                    validator.TypeValidator(int),
                ),
            },
            'sys_key_decrease': {
                'base_str': ':SYST:KEY:DECR',
                'validators': (
                    validator.TypeValidator(int),
                ),
            },
            'sys_poweron_config': {
                'base_str': ':SYST:PON',
                'validators': (
                    common_validators.on_off,
                ),
            },
            'sys_power_on_status': {
                'base_str': ':SYST:PSTATUS',
                'validators': (
                    validator.OptionValidator(('default','open')),
                ),
            },
            'sys_option_install': {
                'base_str': ':SYST:OPT:INST',
                'validators': (
                    validator.TypeValidator(str),
                ),
            },
            'sys_language': {
                'base_str': ':SYST:LANG',
                'validators': (
                    validator.OptionValidator( 
                     ('schinese','tchinese','english','portuguese',
                     'german','polish','korean','japanese','french',
                     'russian'
                    )),
                ),
            },
            'sys_screensaver_timer': {
                'base_str': ':SYST:SSAV:TIME',
                'validators': (
                    validator.OptionValidator(
                        ('1min','2min','5min','15min','30min',
                         '45min','60min','2hour','5hour','off')
                    ),
                ),
            },
            'sys_usb_device_mode': {
                'base_str': ':SYST:UDEV',
                'validators': (
                    validator.OptionValidator(('computer','pictbridge')),
                ),
            },
        }
    }
}
