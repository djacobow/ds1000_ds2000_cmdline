RIGOL_CONFIG = {
    'simple_0_args': {
        'id': {
            'cmd': '*IDN?',
        },
        'reset': {
            'cmd': '*RST',
        },
        'self_test': {
            'cmd': '*TST?',
        },
        'auto': {
            'cmd': ':AUTOscale',
        },
        'clear': {
            'cmd': ':CLEar',
        },
        'run': {
            'cmd': ':RUN',
        },
        'stop': {
            'cmd': ':STOP',
        },
        'single': {
            'cmd': ':SINGle',
        },
        'force_trigger': {
            'cmd': ':TFORce',
        },
        'trig_status': {
            'cmd': ':TRIG:STAT?',
        },
        'trig_position': {
            'cmd': ':TRIG:POS?',
        },
        'sample_rate': {
            'cmd': ':ACQ:SRAT?',
        },

    },

    'simple_2_args': {
        'ch_scale': {
            'q_str':   ':CHAN{a0}:SCAL?',
            'set_str': ':CHAN{a0}:SCAL {a1}',
            'validators': (
                ((int,), (1,2,3,4)),
                ((float,int,), (0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100)),
            ),
            'rtype': 'float',
        },
        'ch_probe': {
            'q_str': ':CHAN{a0}:PROB?',
            'set_str': ':CHAN{a0}:PROB {a1}',
            'validators': (
                ((int,), (1,2,4,5)),
                ((float,int,), (0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100)),
            ),
            'rtype': 'float',
        },
        'ch_display': {
            'q_str': ':CHAN{a0}:DISP?',
            'set_str': ':CHAN{a0}:DISP {a1}',
            'validators': (
                ((int,), (1,2,3,4)),
                ((str,int), (1,0,'on','off')),
            ),
        },
        'ch_bwlimit': {
            'q_str': ':CHAN{a0}:BWL?',
            'set_str': ':CHAN{a0}:BWL {a1}',
            'validators': (
                ((int,), (1,2,3,4)),
                ((str,),('20m','off')),
            ),
        },
        'ch_coupling': {
            'q_str': ':CHAN{a0}:COUP?',
            'set_str': ':CHAN{a0}:COUP {a1}',
            'validators': (
                ((int,), (1,2,3,4)),
                ((str,),('ac','dc','gnd')),
           ),
        },
        'ch_invert': {
            'q_str': ':CHAN{a0}:INV?',
            'set_str': ':CHAN{a0}:INV {a1}',
            'validators': (
                ((int,), (1,2,3,4)),
                ((str,int),('on','off','1','0',1,0)),
            ),
            'rtype': 'int',
        },
        'ch_vernier': {
            'q_str': ':CHAN{a0}:VERN?',
            'set_str': ':CHAN{a0}:VERN {a1}',
            'validators': (
                ((int,), (1,2,3,4)),
                ((str,), ('on','off','1','0',1,0)),
            ),
            'rtype': 'int',
        },
        'ch_offset': {
            'q_str': ':CHANnel{a0}:OFFSet?',
            'set_str': ':CHANnel{a0}:OFFSet {a1}',
            'validators': (
                ((int,), (1,2,3,4)),
                ((float,),None),
            ),
            'rtype': 'float',
        },
    },

    'simple_1_args': {
        'disp_type': {
            'base_str': ':DISP:TYPE',
            'validators': (
                ((str,),('vectors','dots')),
            ),
        },
        'disp_grading_time': {
            'base_str': ':DISP:GRAD:TIME',
            'validators': (
                ((str,float,int), ('min','inf','infinite',0.1,0.2,0.5,1,5,10)),
            ),
        },
        'disp_wave_brightness': {
            'base_str': ':DISP:WBR',
            'validators': (
                ( (int,), lambda x : 0 < x and x < 100 ),
            ),
        },
        'disp_grid_brightness': {
            'base_str': ':DISP:GBR',
            'validators': (
                ((int,), lambda x : 0 < x and x < 100),
            ),
        },
        'disp_grid': {
            'base_str': ':DISP:GRID',
            'validators': (
                ((str,), ('full','half','none')),
            ),
        },
        'horiz_delay': {
            'base_str': ':TIM:DEL:ENAB',
            'validators': (
                ((str,int,), (1,0,'on','off')),
            ),
        },
        'horiz_delay_offset': {
            'base_str': ':TIM:DEL:OFFS',
            'validators': (
                ((float,int),None),
            ),
        },
        'horiz_offset': {
            'base_str': ':TIM:MAIN:OFFS',
            'validators': (
                ((float,int),None),
            ),
        },
        'horiz_mode': {
            'base_str': ':TIM:MODE',
            'validators': (
                ((str,),('main','xy','roll')),
            ),
        },
        'horiz_scale': {
            'base_str': ':TIMebase:MAIN:SCALe',
            'validators': (
                ((float,int,),
                    (
                        5e-9,
                        1e-8, 2e-8, 5e-8,
                        1e-7, 2e-7, 5e-7,
                        1e-6, 2e-6, 5e-6,
                        1e-5, 2e-5, 5e-5,
                        1e-4, 2e-4, 5e-4,
                        1e-3, 2e-3, 5e-3,
                        1e-2, 2e-2, 5e-2,
                        1e-1, 2e-1, 5e-1,
                        1, 2, 5,
                        10, 20, 50,
                    ),
                ),
            ),
            'rtype': 'float',
        },
        'trig_mode': {
            'base_str': ':TRIG:MODE',
            'validators': (
                ((str,),
                 ('edge','puls','runt','wind','nedg','slop','vid','patt','del',
                  'tim','dur','shol','rs232','iic','spi'),
                ),
            ),
        },
        'trig_coupling': {
            'base_str': ':TRIG:COUP',
            'validators': (
                ((str,), ('ac','dc','lfreject','hfreject')),
            ),
        },
        'trig_coupling': {
            'base_str': ':TRIG:SWE',
            'validators': (
                ((str,), ('auto','normal','single')),
            ),
        },
        'trig_holdoff': {
            'base_str': ':TRIG:SWE',
            'validators': (
                ((float,int), lambda x: 16e-9 < x and x < 10),
            ),
            'rtype': 'float',
        },
        'trig_noise_reject': {
            'base_str': ':TRIG:NREJ',
            'validators': (
                ((str,int), (1,0,"on","off")),
            ),
        },
        'trig_source': {
            'base_str': ':TRIG:EDG:SOUR',
            'set_str': ':TRIG:EDG:SOUR {a0}',
            'validators': (
                ((str), ('chan1','chan2','chan3','chan4','ac')),
            ),
        },
        'trig_slope': {
            'base_str': ':TRIG:EDG:SLOP',
            'set_str': ':TRIG:EDG:SLOP {a0}',
            'validators': (
                ((str), ('positive','negative','rfali')),
            ),
        },
        'trig_level': {
            'base_str': ':TRIG:EDG:LEV',
            'validators': (
                ((float,int), None),
            ),
            'rtype': 'float',
        },
        'acq_average': {
            'base_str': ':ACQ:AVER',
            'validators': (
                ((int,), None),
            ),
            'rtype': 'int',
        },
        'acq_depth': {
            'base_str': ':ACQ:MDEPTH',
            'validators': (
                ((int,), None),
            ),
            'rtype': 'int',
        },
        'acq_type': {
            'base_str': ':ACQ:TYPE',
            'validators': (
                ((str,), ('normal','averages','peak','hresolution')),
            ),
        },
    }
}

