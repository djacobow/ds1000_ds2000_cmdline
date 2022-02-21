
from . import personalities

personality_configs = {
    'ds1k': (
        personalities.ds1k.acquire.CONFIG,
        personalities.ds1k.channel.CONFIG,
        personalities.ds1k.cursor.CONFIG,
        personalities.ds1k.decoder.CONFIG,
        personalities.ds1k.display.CONFIG,
        personalities.ds1k.globalcmds.CONFIG,
        personalities.ds1k.measure.CONFIG,
        personalities.ds1k.horizontal.CONFIG,
        personalities.ds1k.network.CONFIG,
        personalities.ds1k.storage.CONFIG,
        personalities.ds1k.system.CONFIG,
        personalities.ds1k.trigger.CONFIG,
    ),
    'ds2k': (
        personalities.ds2k.globalcmds.CONFIG,
        personalities.ds2k.acquire.CONFIG,
        personalities.ds2k.channel.CONFIG,
        personalities.ds2k.cursor.CONFIG,
        personalities.ds2k.decoder.CONFIG,
        personalities.ds2k.display.CONFIG,
        personalities.ds2k.horizontal.CONFIG,
        personalities.ds2k.network.CONFIG,
        personalities.ds2k.system.CONFIG,
        personalities.ds2k.trigger.CONFIG,
    ),
}

RIGOL_CONFIG = {}

for personality, modules_configs in personality_configs.items():
    if not personality in RIGOL_CONFIG:
        RIGOL_CONFIG[personality] = {}
    for m in modules_configs:
        for group_type, group_config in m.items():
            for cmd_type in ('simple_0_args','simple_1_args','simple_2_args'):
                if cmd_type in group_config:
                    if not cmd_type in RIGOL_CONFIG[personality]:
                        RIGOL_CONFIG[personality][cmd_type] = {}
                    if not group_type in RIGOL_CONFIG[personality][cmd_type]:
                        RIGOL_CONFIG[personality][cmd_type][group_type] = {}
                    RIGOL_CONFIG[personality][cmd_type][group_type]['commands'] = group_config[cmd_type]
                    if not 'name' in RIGOL_CONFIG[personality][cmd_type][group_type]:
                        RIGOL_CONFIG[personality][cmd_type][group_type]['name'] = group_config['name']

