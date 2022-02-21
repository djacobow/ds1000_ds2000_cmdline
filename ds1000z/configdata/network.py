from . import validators

CONFIG = {
    'network': {
        'name': 'Network Commands',
        'simple_0_args': {
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
        },
        'simple_1_args': {
            'net_dhcp': {
                'base_str': ':LAN:DHCP',
                'validators': (
                    validators.on_off,
                ),
            },
            'net_autoip': {
                'base_str': ':LAN:AUToip',
                'validators': (
                    validators.on_off,
                ),
            },
            'net_gateway': {
                'base_str': ':LAN:GATeway',
                'validators': (
                    validators.ip_addr,
                ),
            },
            'net_dns': {
                'base_str': ':LAN:DNS',
                'validators': (
                    validators.ip_addr,
                ),
            },
            'net_manual': {
                'base_str': ':LAN:MANual',
                'validators': (
                    validators.on_off,
                ),
            },
            'net_ipaddr': {
                'base_str': ':LAN:IPAD',
                'validators': (
                    validators.ip_addr,
                ),
            },
            'net_subnet': {
                'base_str': ':LAN:SMASk',
                'validators': (
                    validators.ip_addr,
                ),
            },
        }
    }
}
