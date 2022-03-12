
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
        personalities.ds1k.waveform.CONFIG,
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
            new_commands = group_config.get('commands',{})
            if not group_type in RIGOL_CONFIG[personality]:
                RIGOL_CONFIG[personality][group_type] = {}
            if not 'commands' in RIGOL_CONFIG[personality][group_type]:
                RIGOL_CONFIG[personality][group_type]['commands'] = {}
            RIGOL_CONFIG[personality][group_type]['commands'].update(new_commands)
            if not 'name' in RIGOL_CONFIG[personality][group_type]:
                RIGOL_CONFIG[personality][group_type]['name'] = group_config['name']

