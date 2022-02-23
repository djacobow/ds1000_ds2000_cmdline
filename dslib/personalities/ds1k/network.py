from ... import argspec
from . import common_argspecs

CONFIG = {
    'network': {
        'name': 'Network Commands',
        'commands': {
            'net_mac_addr': {
                'help': 'Get the unit\'s MAC address',
                'cmd': ':LAN:MAC?',
            },
            'net_initiate': {
                'cmd': ':LAN:INIT',
            },
            'net_status': {
                'help': 'Get the unit\'s network status',
                'cmd': ':LAN:STAT?',
            },
            'net_visa': {
                'help': 'Get the unit\'s VISA identifications string',
                'cmd': ':LAN:VISA?',
            },
            'net_apply': {
                'help': 'Apply changes to network settings.',
                'cmd': ':LAN:APPLy',
            },
            'net_dhcp': {
                'help': 'Enable DHCP client',
                'base_str': ':LAN:DHCP',
                'argspecs': (
                    common_argspecs.on_off,
                ),
            },
            'net_autoip': {
                'help': 'Enable Auto-IP (picking own address)',
                'base_str': ':LAN:AUToip',
                'argspecs': (
                    common_argspecs.on_off,
                ),
            },
            'net_gateway': {
                'help': 'Set or get the gateway address',
                'base_str': ':LAN:GATeway',
                'argspecs': (
                    common_argspecs.ip_addr,
                ),
            },
            'net_dns': {
                'help': 'Get or set the DNS address',
                'base_str': ':LAN:DNS',
                'argspecs': (
                    common_argspecs.ip_addr,
                ),
            },
            'net_manual': {
                'help': 'Manually configure network',
                'base_str': ':LAN:MANual',
                'argspecs': (
                    common_argspecs.on_off,
                ),
            },
            'net_ipaddr': {
                'help': 'Get or set the current IP address',
                'base_str': ':LAN:IPAD',
                'argspecs': (
                    common_argspecs.ip_addr,
                ),
            },
            'net_subnet': {
                'help': 'Get or set the subnet mask',
                'base_str': ':LAN:SMASk',
                'argspecs': (
                    common_argspecs.ip_addr,
                ),
            },
        }
    }
}
