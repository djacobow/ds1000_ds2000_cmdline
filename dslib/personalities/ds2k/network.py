from ... import argspec
from . import common_argspecs

CONFIG = {
    'network': {
        'name': 'Network Commands',
        'commands': {
            'net_mac_addr': {
                'cmd': ':LAN:MAC?',
            },
            'net_initiate': {
                'cmd': ':LAN:INIT',
            },
            'net_status': {
                'cmd': ':LAN:STAT?',
            },
            'net_visa': {
                'cmd': ':LAN:VISA?',
            },
            'net_apply': {
                'cmd': ':LAN:APPLy',
            },
            'net_dhcp': {
                'base_str': ':LAN:DHCP',
                'argspecs': (
                    common_argspecs.on_off,
                ),
            },
            'net_autoip': {
                'base_str': ':LAN:AUToip',
                'argspecs': (
                    common_argspecs.on_off,
                ),
            },
            'net_gateway': {
                'base_str': ':LAN:GATeway',
                'argspecs': (
                    common_argspecs.ip_addr,
                ),
            },
            'net_dns': {
                'base_str': ':LAN:DNS',
                'argspecs': (
                    common_argspecs.ip_addr,
                ),
            },
            'net_manual': {
                'base_str': ':LAN:MANual',
                'argspecs': (
                    common_argspecs.on_off,
                ),
            },
            'net_ipaddr': {
                'base_str': ':LAN:IPAD',
                'argspecs': (
                    common_argspecs.ip_addr,
                ),
            },
            'net_subnet': {
                'base_str': ':LAN:SMASk',
                'argspecs': (
                    common_argspecs.ip_addr,
                ),
            },
        }
    }
}
