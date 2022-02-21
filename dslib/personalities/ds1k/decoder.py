from . import validators

CONFIG = {
    'decoder': {
        'name': 'Decoder Shared',
        'simple_2_args': {
            'decoder_mode': {
                'q_str':   ':DEC{a0}:MODE?',
                'set_str': ':DEC{a0}:MODE {a1}',
                'validators': (
                    validators.decoder_number,
                    ((str,), ('parallel','uart','spi','iic')),
                ),
            },
            'decoder_display': {
                'q_str':   ':DEC{a0}:DISP?',
                'set_str': ':DEC{a0}:DISP {a1}',
                'validators': (
                    validators.decoder_number,
                    validators.on_off,
                ),
            },
            'decoder_format': {
                'q_str':   ':DEC{a0}:FORM?',
                'set_str': ':DEC{a0}:FORM {a1}',
                'validators': (
                    validators.decoder_number,
                    ((str,), ('hex','ascii','dec','bin','line')),
                ),
            },
            'decoder_position': {
                'q_str':   ':DEC{a0}:POS?',
                'set_str': ':DEC{a0}:POS {a1}',
                'validators': (
                    validators.decoder_number,
                    ((int,), lambda x : 50 <= x and x <= 350),
                ),
                'rtype': 'int',
            },
            'decoder_threshold': {
                'q_str':   ':DEC{a0}:THRE:CHAN{a1}?',
                'set_str': ':DEC{a0}:THRE:CHAN{a1} {a2}',
                'validators': (
                    validators.decoder_number,
                    validators.channel_number,
                    ((float,), None ),
                ),
                'rtype': 'float',
            },
            'decoder_threshold_auto': {
                'q_str':   ':DEC{a0}:THRE:AUTO?',
                'set_str': ':DEC{a0}:THRE:AUTO {a1}',
                'validators': (
                    validators.decoder_number,
                    validators.on_off,
                ),
            },
            'decoder_config_label': {
                'q_str':   ':DEC{a0}:CONF:LABel?',
                'set_str': ':DEC{a0}:CONF:LABel {a1}',
                'validators': (
                    validators.decoder_number,
                    validators.on_off,
                ),
            },
            'decoder_config_line': {
                'q_str':   ':DEC{a0}:CONF:LINE?',
                'set_str': ':DEC{a0}:CONF:LINE {a1}',
                'validators': (
                    validators.decoder_number,
                    validators.on_off,
                ),
            },
            'decoder_config_format': {
                'q_str':   ':DEC{a0}:CONF:FORM?',
                'set_str': ':DEC{a0}:CONF:FORM {a1}',
                'validators': (
                    validators.decoder_number,
                    validators.on_off,
                ),
            },
            'decoder_config_endian': {
                'q_str':   ':DEC{a0}:CONF:END?',
                'set_str': ':DEC{a0}:CONF:END {a1}',
                'validators': (
                    validators.decoder_number,
                    validators.on_off,
                ),
            },
            'decoder_config_width': {
                'q_str':   ':DEC{a0}:CONF:WIDth?',
                'set_str': ':DEC{a0}:CONF:WIDth {a1}',
                'validators': (
                    validators.decoder_number,
                    validators.on_off,
                ),
            },
        },
    },
    'decoder_uart': {
        'name': 'UART Decoder Settings',
        'simple_2_args': {
            'decoder_uart_tx_source': {
                'q_str':   ':DEC{a0}:UART:TX?',
                'set_str': ':DEC{a0}:UART:TX {a1}',
                'validators': (
                    validators.decoder_number,
                    validators.decoder_source,
                ),
            },
            'decoder_uart_rx_source': {
                'q_str':   ':DEC{a0}:UART:RX?',
                'set_str': ':DEC{a0}:UART:RX {a1}',
                'validators': (
                    validators.decoder_number,
                    validators.decoder_source,
                ),
            },
            'decoder_uart_polarity': {
                'q_str':   ':DEC{a0}:UART:POL?',
                'set_str': ':DEC{a0}:UART:POL {a1}',
                'validators': (
                    validators.decoder_number,
                    validators.neg_pos,
                ),
            },
            'decoder_uart_endian': {
                'q_str':   ':DEC{a0}:UART:END?',
                'set_str': ':DEC{a0}:UART:END {a1}',
                'validators': (
                    validators.decoder_number,
                    ((str,), ('lsb','msb')),
                ),
            },
            'decoder_uart_baud': {
                'q_str':   ':DEC{a0}:UART:BAUD?',
                'set_str': ':DEC{a0}:UART:BAUD {a1}',
                'validators': (
                    validators.decoder_number,
                    ((int,), lambda x : 110 <= x and x <= 20e6),
                ),
            },
            'decoder_uart_width': {
                'q_str':   ':DEC{a0}:UART:WIDTh?',
                'set_str': ':DEC{a0}:UART:WIDTh {a1}',
                'validators': (
                    validators.decoder_number,
                    ((int,), lambda x : 5 <= x and x <= 8),
                ),
            },
            'decoder_uart_width': {
                'q_str':   ':DEC{a0}:UART:STOP?',
                'set_str': ':DEC{a0}:UART:STOP {a1}',
                'validators': (
                    validators.decoder_number,
                    ((int,float), lambda x : x in (1, 1.5, 2)),
                ),
            },
            'decoder_uart_parity': {
                'q_str':   ':DEC{a0}:UART:PARity?',
                'set_str': ':DEC{a0}:UART:PARity {a1}',
                'validators': (
                    validators.decoder_number,
                    ((str,), ('none','even','odd')),
                ),
            },
        },
    },
    'decoder_iic': {
        'name': 'Decoder I2C Settings',
        'simple_2_args': {
            'decoder_iic_scl': {
                'q_str':   ':DEC{a0}:IIC:CLK?',
                'set_str': ':DEC{a0}:IIC:CLK {a1}',
                'validators': (
                    validators.decoder_number,
                    validators.decoder_source,
                ),
            },
            'decoder_iic_sda': {
                'q_str':   ':DEC{a0}:IIC:DATA?',
                'set_str': ':DEC{a0}:IIC:DATA {a1}',
                'validators': (
                    validators.decoder_number,
                    validators.decoder_source,
                ),
            },
            'decoder_iic_addr': {
                'q_str':   ':DEC{a0}:UART:ADDR?',
                'set_str': ':DEC{a0}:UART:ADDR {a1}',
                'validators': (
                    validators.decoder_number,
                    ((str,), ('normal','rw')),
                ),
            },
        },
    },
    'decoder_spi': {
        'name': 'Decoder SPI Settings',
        'simple_2_args': {
            'decoder_spi_mclk': {
                'q_str':   ':DEC{a0}:SPI:CLK?',
                'set_str': ':DEC{a0}:SPI:CLK {a1}',
                'validators': (
                    validators.decoder_number,
                    validators.decoder_source,
                ),
            },
            'decoder_spi_miso': {
                'q_str':   ':DEC{a0}:SPI:MISO?',
                'set_str': ':DEC{a0}:SPI:MISO {a1}',
                'validators': (
                    validators.decoder_number,
                    validators.decoder_source,
                ),
            },
            'decoder_spi_mosi': {
                'q_str':   ':DEC{a0}:SPI:MOSI?',
                'set_str': ':DEC{a0}:SPI:MOSI {a1}',
                'validators': (
                    validators.decoder_number,
                    validators.decoder_source,
                ),
            },
            'decoder_spi_cs': {
                'q_str':   ':DEC{a0}:SPI:CS?',
                'set_str': ':DEC{a0}:SPI:CS {a1}',
                'validators': (
                    validators.decoder_number,
                    validators.decoder_source,
                ),
            },
            'decoder_spi_cs_polarity': {
                'q_str':   ':DEC{a0}:SPI:SEL?',
                'set_str': ':DEC{a0}:SPI:SEL {a1}',
                'validators': (
                    validators.decoder_number,
                    ((str,), ('ncs','cs')),
                ),
            },
            'decoder_spi_cs_polarity': {
                'q_str':   ':DEC{a0}:SPI:MODE?',
                'set_str': ':DEC{a0}:SPI:MODE {a1}',
                'validators': (
                    validators.decoder_number,
                    ((str,), ('cs','timeout')),
                ),
            },
            'decoder_spi_timeout': {
                'q_str':   ':DEC{a0}:SPI:TIMeout?',
                'set_str': ':DEC{a0}:SPI:TIMeout {a1}',
                'validators': (
                    validators.decoder_number,
                    ((int,float,), None),
                ),
            },
            'decoder_spi_polarity': {
                'q_str':   ':DEC{a0}:SPI:POLarity?',
                'set_str': ':DEC{a0}:SPI:POLarity {a1}',
                'validators': (
                    validators.decoder_number,
                    validators.neg_pos,
                ),
            },
            'decoder_spi_edge': {
                'q_str':   ':DEC{a0}:SPI:EDGE?',
                'set_str': ':DEC{a0}:SPI:EDGE {a1}',
                'validators': (
                    validators.decoder_number,
                    ((str,), ('rise','fall')),
                ),
            },
            'decoder_spi_endian': {
                'q_str':   ':DEC{a0}:SPI:ENDian?',
                'set_str': ':DEC{a0}:SPI:ENDian {a1}',
                'validators': (
                    validators.decoder_number,
                    ((str,), ('lsb','msb')),
                ),
            },
            'decoder_spi_width': {
                'q_str':   ':DEC{a0}:SPI:WIDTh?',
                'set_str': ':DEC{a0}:SPI:WIDTh {a1}',
                'validators': (
                    validators.decoder_number,
                    ((int,), lambda x : x <= 8 and x <= 32),
                ),
            },
        },
    },
    'decoder_parallel': {
    'name': 'Parallel Decoder Settings',
        'simple_2_args': {
            'decoder_parallel_clk': {
                'q_str':   ':DEC{a0}:PAR:CLK?',
                'set_str': ':DEC{a0}:PAR:CLK {a1}',
                'validators': (
                    validators.decoder_number,
                    validators.decoder_source,
                ),
            },
            'decoder_parallel_source': {
                'q_str':   ':DEC{a0}:PAR:SOUR?',
                'set_str': ':DEC{a0}:PAR:SOUR {a1}',
                'validators': (
                    validators.decoder_number,
                    validators.decoder_source,
                ),
            },
            'decoder_parallel_edge': {
                'q_str':   ':DEC{a0}:PAR:EDGE?',
                'set_str': ':DEC{a0}:PAR:EDGE {a1}',
                'validators': (
                    validators.decoder_number,
                    ((str,), ('rise','fall','both')),
                ),
            },
            'decoder_parallel_width': {
                'q_str':   ':DEC{a0}:PAR:WIDTh?',
                'set_str': ':DEC{a0}:PAR:WIDTh {a1}',
                'validators': (
                    validators.decoder_number,
                    ((str,), lambda x: 1 <= x and x <= 16),
                ),
            },
            'decoder_parallel_bitsel': {
                'q_str':   ':DEC{a0}:PAR:BITX?',
                'set_str': ':DEC{a0}:PAR:BITX {a1}',
                'validators': (
                    validators.decoder_number,
                    ((str,), lambda x: 1 <= x and x <= 16),
                ),
            },
            'decoder_parallel_polarity': {
                'q_str':   ':DEC{a0}:PAR:POLarity?',
                'set_str': ':DEC{a0}:PAR:POLarity {a1}',
                'validators': (
                    validators.decoder_number,
                    validators.neg_pos,
                ),
            },
            'decoder_parallel_noise_reject': {
                'q_str':   ':DEC{a0}:PAR:NREJect?',
                'set_str': ':DEC{a0}:PAR:NREJect {a1}',
                'validators': (
                    validators.decoder_number,
                    validators.on_off,
                ),
            },
            'decoder_parallel_noise_reject_time': {
                'q_str':   ':DEC{a0}:PAR:NRTime?',
                'set_str': ':DEC{a0}:PAR:NRTime {a1}',
                'validators': (
                    validators.decoder_number,
                    ((float,), lambda x: 0 < x and x <= 0.1),
                ),
            },
            'decoder_parallel_compensation_time': {
                'q_str':   ':DEC{a0}:PAR:CCOM?',
                'set_str': ':DEC{a0}:PAR:CCOM {a1}',
                'validators': (
                    validators.decoder_number,
                    ((float,), lambda x: -0.1 <= x and x <= 0.1),
                ),
            },
            'decoder_parallel_plot': {
                'q_str':   ':DEC{a0}:PAR:PLOT?',
                'set_str': ':DEC{a0}:PAR:PLOT {a1}',
                'validators': (
                    validators.decoder_number,
                    validators.on_off,
                ),
            },
        },
    },
}
