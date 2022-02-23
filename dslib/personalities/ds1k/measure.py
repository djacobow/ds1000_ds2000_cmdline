from ... import argspec
from . import common_argspecs

onevar_measurements = argspec.OptionArgSpec(
    ('vmax','vmin','vpp','vtop','vbase','vamp','vavg',
     'vrms','overshoot','marea','mparea','preshoot','period',
     'frequency','rtime','ftime','pwidth','nwidth','pduty','nduty',
     'tvmax','tvmin','pslewrate','nslewrate','vupper','vmid','vlower',
     'variance','pvrms','ppulses','npulses','pedges','nedges')
)

summary_type = argspec.OptionArgSpec(('maximum','minimum','current','averages','deviation'))

CONFIG = {
    'measure': {
        'name': 'Measurements',
        'commands': {
            'measure_counter_value': {
                'cmd': 'MEAS:COUN:VAL?',
            },    
            'measure_clear': {
                'cmd': 'MEAS:CLE',
            },    
            'measure_recover': {
                'cmd': 'MEAS:REC',
            },    
            'measure_sources': {
                'cmd': 'MEAS:AMS?',
            },    
            'measure_statistic_reset': {
                'cmd': 'MEAS:STAT:RESet',
            },    
            'measure_source': {
                'base_str': ':MEAS:SOURce',
                'argspecs': (
                    common_argspecs.measure_source,
                ),
            },
            'measure_counter_source': {
                'base_str': ':MEAS:COUN:SOURce',
                'argspecs': (
                    common_argspecs.decoder_source, 
                ),
            },
            'measure_disp_all': {
                'base_str': ':MEAS:ADIS',
                'argspecs': (
                    common_argspecs.on_off,
                ),
            },
            'measure_setup_thresh_max': {
                'base_str': ':MEAS:SET:MAX',
                'argspecs': (
                    argspec.RangeArgSpec(7,95,int),
                ),
            },
            'measure_setup_thresh_mid': {
                'base_str': ':MEAS:SET:MID',
                'argspecs': (
                    argspec.RangeArgSpec(6,94,int),
                ),
            },
            'measure_setup_thresh_min': {
                'base_str': ':MEAS:SET:MIN',
                'argspecs': (
                    argspec.RangeArgSpec(5,93,int),
                ),
            },
            'measure_setup_phase_b_source': {
                'base_str': ':MEAS:SET:PSB',
                'argspecs': (
                    common_argspecs.measure_source,
                ),
            },
            'measure_setup_delay_a_source': {
                'base_str': ':MEAS:SET:DSA',
                'argspecs': (
                    common_argspecs.measure_source,
                ),
            },
            'measure_setup_delay_b_source': {
                'base_str': ':MEAS:SET:DSB',
                'argspecs': (
                    common_argspecs.measure_source,
                ),
            },
            'measure_statistic_display': {
                'base_str': ':MEAS:STAT:DISP',
                'argspecs': (
                    common_argspecs.on_off,
                ),
            },
            'measure_statistic_mode': {
                'base_str': ':MEAS:STAT:MODE',
                'argspecs': (
                    argspec.OptionArgSpec(('difference','extremum')),
                ),
            },
            'measure_statistic_set_item': {
                'set_str': ':MEAS:STAT:ITEM {a0},{a1}',
                'argspecs': (
                    onevar_measurements,
                    common_argspecs.measure_source,
                ),
            },
            'measure_statistic_get_item': {
                'set_str': ':MEAS:STAT:ITEM {a0},{a1},{a2}',
                'argspecs': (
                    summary_type,
                    onevar_measurements,
                    common_argspecs.measure_source,
                ),
            },
            'measure_item': {
                'set_str': ':MEAS:ITEM {a0},{a1}',
                'argspecs': (
                    onevar_measurements,
                    common_argspecs.measure_source,
                ),
            },
        },
    },
}


