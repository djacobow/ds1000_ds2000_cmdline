from ... import validator
from . import common_validators

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
                'validators': (
                    common_validators.on_off,
                ),
            },
            'net_autoip': {
                'base_str': ':LAN:AUToip',
                'validators': (
                    common_validators.on_off,
                ),
            },
            'net_gateway': {
                'base_str': ':LAN:GATeway',
                'validators': (
                    common_validators.ip_addr,
                ),
            },
            'net_dns': {
                'base_str': ':LAN:DNS',
                'validators': (
                    common_validators.ip_addr,
                ),
            },
            'net_manual': {
                'base_str': ':LAN:MANual',
                'validators': (
                    common_validators.on_off,
                ),
            },
            'net_ipaddr': {
                'base_str': ':LAN:IPAD',
                'validators': (
                    common_validators.ip_addr,
                ),
            },
            'net_subnet': {
                'base_str': ':LAN:SMASk',
                'validators': (
                    common_validators.ip_addr,
                ),
            },
        }
    }
}
