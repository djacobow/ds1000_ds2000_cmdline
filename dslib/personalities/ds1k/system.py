from ... import argspec
from . import common_argspecs

def storeSetup(rs, args):
    rs.saveSetup(args[0] if len(args) else None)

def loadSetup(rs, args):
    rs.restoreSetup(args[0])

CONFIG = {
    'system': {
        'name': 'System Commands',
        'commands': {
             'sys_store_setup': {
                 'help': 'Store complete scope state to file.',
                 'func': storeSetup,
                 'argspecs': (
                    argspec.TypeArgSpec((str,None)),
                 ),
             },
             'sys_save_setup': {
                 'help': 'Restore complete scope state from file.',
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
             'sys_enable_autoscale': {
                 'help': 'Enable or disable the autoscale feature',
                 'base_str': ':SYST:AUT',
                 'argspecs': (
                     common_argspecs.on_off,
                 ),
             },
             'sys_enable_beep': {
                 'help': 'Enable or disable system beeps',
                 'base_str': ':SYST:BEEP',
                 'argspecs': (
                     common_argspecs.on_off,
                 ),
             },
             'sys_lock_keyboard': {
                 'help': 'Lock or unlock the control panel keys',
                 'base_str': ':SYST:LOCK',
                 'argspecs': (
                     argspec.OptionArgSpec(('latest','default')),
                 ),
             },
             'sys_poweron_config': {
                 'help': 'Rembmer last settings on poweron',
                 'base_str': ':SYST:PON',
                 'argspecs': (
                     common_argspecs.on_off,
                 ),
             },
             'sys_option_install': {
                 'help': 'Install new software options with key',
                 'base_str': ':SYST:OPT:INST',
                 'argspecs': (
                     argspec.TypeArgSpec(str),
                 ),
             },
             'sys_language': {
                 'help': 'Set display language (does not affect API)',
                 'base_str': ':SYST:LANG',
                 'argspecs': (
                     argspec.OptionArgSpec(
                         ('schinese','tchinese','english','portuguese',
                          'german','polish','korean','japanese','french',
                          'russian'
                         )
                     ),
                 ),
             },
         }
     }
}
