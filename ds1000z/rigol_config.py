
from . import configdata

modules_configs = (
    configdata.acquire.CONFIG,
    configdata.channel.CONFIG,
    configdata.cursor.CONFIG,
    configdata.decoder.CONFIG,
    configdata.display.CONFIG,
    configdata.globalcmds.CONFIG,
    configdata.measure.CONFIG,
    configdata.horizontal.CONFIG,
    configdata.network.CONFIG,
    configdata.storage.CONFIG,
    configdata.system.CONFIG,
    configdata.trigger.CONFIG,
)

RIGOL_CONFIG = {}

for m in modules_configs:
    for group_type, group_config in m.items():
       for cmd_type in ('simple_0_args','simple_1_args','simple_2_args'):
           if cmd_type in group_config:
               if not cmd_type in RIGOL_CONFIG:
                   RIGOL_CONFIG[cmd_type] = {}
               if not group_type in RIGOL_CONFIG[cmd_type]:
                   RIGOL_CONFIG[cmd_type][group_type] = {}
               RIGOL_CONFIG[cmd_type][group_type]['commands'] = group_config[cmd_type]
               if not 'name' in RIGOL_CONFIG[cmd_type][group_type]:
                   RIGOL_CONFIG[cmd_type][group_type]['name']     = group_config['name']

