from . import validators

onevar_measurements = (
    (str,),
    ('vmax','vmin','vpp','vtop','vbase','vamp','vavg',
     'vrms','overshoot','marea','mparea','preshoot','period',
     'frequency','rtime','ftime','pwidth','nwidth','pduty','nduty',
     'tvmax','tvmin','pslewrate','nslewrate','vupper','vmid','vlower',
     'variance','pvrms','ppulses','npulses','pedges','nedges')
)

summary_type = ((str,), ('maximum','minimum','current','averages','deviation'))

CONFIG = {
    'measure': {
        'name': 'Measurements',
        'simple_0_args': {
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
         },
        'simple_1_args': {
            'measure_source': {
                'base_str': ':MEAS:SOURce',
                'validators': (
                    validators.measure_source,
                ),
            },
            'measure_counter_source': {
                'base_str': ':MEAS:COUN:SOURce',
                'validators': (
                    validators.decoder_source, 
                ),
            },
            'measure_disp_all': {
                'base_str': ':MEAS:ADIS',
                'validators': (
                    validators.on_off,
                ),
            },
            'measure_setup_thresh_max': {
                'base_str': ':MEAS:SET:MAX',
                'validators': (
                    ((int,), lambda x: 7 <= x and x < 95),
                ),
            },
            'measure_setup_thresh_mid': {
                'base_str': ':MEAS:SET:MID',
                'validators': (
                    ((int,), lambda x: 6 <= x and x < 94),
                ),
            },
            'measure_setup_thresh_min': {
                'base_str': ':MEAS:SET:MIN',
                'validators': (
                    ((int,), lambda x: 5 <= x and x < 93),
                ),
            },
            'measure_setup_phase_b_source': {
                'base_str': ':MEAS:SET:PSB',
                'validators': (
                    validators.measure_source,
                ),
            },
            'measure_setup_delay_a_source': {
                'base_str': ':MEAS:SET:DSA',
                'validators': (
                    validators.measure_source,
                ),
            },
            'measure_setup_delay_b_source': {
                'base_str': ':MEAS:SET:DSB',
                'validators': (
                    validators.measure_source,
                ),
            },
            'measure_statistic_display': {
                'base_str': ':MEAS:STAT:DISP',
                'validators': (
                    validators.on_off,
                ),
            },
            'measure_statistic_mode': {
                'base_str': ':MEAS:STAT:MODE',
                'validators': (
                    ((str,), ('difference','extremum')),
                ),
            },
        },
        'simple_2_args': {
            'measure_statistic_set_item': {
                'set_str': ':MEAS:STAT:ITEM {a0},{a1}',
                'validators': (
                    onevar_measurements,
                    validators.measure_source,
                ),
            },
            'measure_statistic_get_item': {
                'set_str': ':MEAS:STAT:ITEM {a0},{a1},{a2}',
                'validators': (
                    summary_type,
                    onevar_measurements,
                    validators.measure_source,
                ),
            },
            'measure_item': {
                'set_str': ':MEAS:ITEM {a0},{a1}',
                'validators': (
                    onevar_measurements,
                    validators.measure_source,
                ),
            },
        },
    },
}


