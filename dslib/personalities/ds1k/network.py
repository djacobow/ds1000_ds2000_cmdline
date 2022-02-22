from ... import validator
from . import common_validators

CONFIG = {
    'network': {
        'name': 'Network Commands',
        'simple_0_args': {
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
        },
        'simple_1_args': {
            'net_dhcp': {
                'help': 'Enable DHCP client',
                'base_str': ':LAN:DHCP',
                'validators': (
                    common_validators.on_off,
                ),
            },
            'net_autoip': {
                'help': 'Enable Auto-IP (picking own address)',
                'base_str': ':LAN:AUToip',
                'validators': (
                    common_validators.on_off,
                ),
            },
            'net_gateway': {
                'help': 'Set or get the gateway address',
                'base_str': ':LAN:GATeway',
                'validators': (
                    common_validators.ip_addr,
                ),
            },
            'net_dns': {
                'help': 'Get or set the DNS address',
                'base_str': ':LAN:DNS',
                'validators': (
                    common_validators.ip_addr,
                ),
            },
            'net_manual': {
                'help': 'Manually configure network',
                'base_str': ':LAN:MANual',
                'validators': (
                    common_validators.on_off,
                ),
            },
            'net_ipaddr': {
                'help': 'Get or set the current IP address',
                'base_str': ':LAN:IPAD',
                'validators': (
                    common_validators.ip_addr,
                ),
            },
            'net_subnet': {
                'help': 'Get or set the subnet mask',
                'base_str': ':LAN:SMASk',
                'validators': (
                    common_validators.ip_addr,
                ),
            },
        }
    }
}
