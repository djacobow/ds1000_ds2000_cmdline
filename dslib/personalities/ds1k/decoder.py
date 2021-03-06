from ... import argspec
from . import common_argspecs

CONFIG = {
    'decoder': {
        'name': 'Decoder Shared',
        'commands': {
            'decoder_mode': {
                'q_str':   ':DEC{a0}:MODE?',
                'set_str': ':DEC{a0}:MODE {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.OptionArgSpec(('parallel','uart','spi','iic')),
                ),
            },
            'decoder_display': {
                'q_str':   ':DEC{a0}:DISP?',
                'set_str': ':DEC{a0}:DISP {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.on_off,
                ),
            },
            'decoder_format': {
                'q_str':   ':DEC{a0}:FORM?',
                'set_str': ':DEC{a0}:FORM {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.OptionArgSpec(('hex','ascii','dec','bin','line')),
                ),
            },
            'decoder_position': {
                'q_str':   ':DEC{a0}:POS?',
                'set_str': ':DEC{a0}:POS {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.RangeArgSpec(50,350,int),
                ),
                'rtype': 'int',
            },
            'decoder_threshold': {
                'q_str':   ':DEC{a0}:THRE:CHAN{a1}?',
                'set_str': ':DEC{a0}:THRE:CHAN{a1} {a2}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.channel_number,
                    argspec.TypeArgSpec(float),
                ),
                'rtype': 'float',
            },
            'decoder_threshold_auto': {
                'q_str':   ':DEC{a0}:THRE:AUTO?',
                'set_str': ':DEC{a0}:THRE:AUTO {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.on_off,
                ),
            },
            'decoder_config_label': {
                'q_str':   ':DEC{a0}:CONF:LABel?',
                'set_str': ':DEC{a0}:CONF:LABel {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.on_off,
                ),
            },
            'decoder_config_line': {
                'q_str':   ':DEC{a0}:CONF:LINE?',
                'set_str': ':DEC{a0}:CONF:LINE {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.on_off,
                ),
            },
            'decoder_config_format': {
                'q_str':   ':DEC{a0}:CONF:FORM?',
                'set_str': ':DEC{a0}:CONF:FORM {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.on_off,
                ),
            },
            'decoder_config_endian': {
                'q_str':   ':DEC{a0}:CONF:END?',
                'set_str': ':DEC{a0}:CONF:END {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.on_off,
                ),
            },
            'decoder_config_width': {
                'q_str':   ':DEC{a0}:CONF:WIDth?',
                'set_str': ':DEC{a0}:CONF:WIDth {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.on_off,
                ),
            },
        },
    },
    'decoder_uart': {
        'name': 'UART Decoder Settings',
        'commands': {
            'decoder_uart_tx_source': {
                'q_str':   ':DEC{a0}:UART:TX?',
                'set_str': ':DEC{a0}:UART:TX {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.decoder_source,
                ),
            },
            'decoder_uart_rx_source': {
                'q_str':   ':DEC{a0}:UART:RX?',
                'set_str': ':DEC{a0}:UART:RX {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.decoder_source,
                ),
            },
            'decoder_uart_polarity': {
                'q_str':   ':DEC{a0}:UART:POL?',
                'set_str': ':DEC{a0}:UART:POL {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.neg_pos,
                ),
            },
            'decoder_uart_endian': {
                'q_str':   ':DEC{a0}:UART:END?',
                'set_str': ':DEC{a0}:UART:END {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.OptionArgSpec(('lsb','msb')),
                ),
            },
            'decoder_uart_baud': {
                'q_str':   ':DEC{a0}:UART:BAUD?',
                'set_str': ':DEC{a0}:UART:BAUD {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.RangeArgSpec(110,20e6,int),
                ),
            },
            'decoder_uart_width': {
                'q_str':   ':DEC{a0}:UART:WIDTh?',
                'set_str': ':DEC{a0}:UART:WIDTh {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.RangeArgSpec(5,8,int),
                ),
            },
            'decoder_uart_stop': {
                'q_str':   ':DEC{a0}:UART:STOP?',
                'set_str': ':DEC{a0}:UART:STOP {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.OptionArgSpec((1,1.5,2),(int,float)),
                ),
            },
            'decoder_uart_parity': {
                'q_str':   ':DEC{a0}:UART:PARity?',
                'set_str': ':DEC{a0}:UART:PARity {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.OptionArgSpec(('none','even','odd')),
                ),
            },
        },
    },
    'decoder_iic': {
        'name': 'Decoder I2C Settings',
        'commands': {
            'decoder_iic_scl': {
                'q_str':   ':DEC{a0}:IIC:CLK?',
                'set_str': ':DEC{a0}:IIC:CLK {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.decoder_source,
                ),
            },
            'decoder_iic_sda': {
                'q_str':   ':DEC{a0}:IIC:DATA?',
                'set_str': ':DEC{a0}:IIC:DATA {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.decoder_source,
                ),
            },
            'decoder_iic_addr': {
                'q_str':   ':DEC{a0}:UART:ADDR?',
                'set_str': ':DEC{a0}:UART:ADDR {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.OptionArgSpec(('normal','rw')),
                ),
            },
        },
    },
    'decoder_spi': {
        'name': 'Decoder SPI Settings',
        'commands': {
            'decoder_spi_mclk': {
                'q_str':   ':DEC{a0}:SPI:CLK?',
                'set_str': ':DEC{a0}:SPI:CLK {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.decoder_source,
                ),
            },
            'decoder_spi_miso': {
                'q_str':   ':DEC{a0}:SPI:MISO?',
                'set_str': ':DEC{a0}:SPI:MISO {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.decoder_source,
                ),
            },
            'decoder_spi_mosi': {
                'q_str':   ':DEC{a0}:SPI:MOSI?',
                'set_str': ':DEC{a0}:SPI:MOSI {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.decoder_source,
                ),
            },
            'decoder_spi_cs': {
                'q_str':   ':DEC{a0}:SPI:CS?',
                'set_str': ':DEC{a0}:SPI:CS {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.decoder_source,
                ),
            },
            'decoder_spi_cs_polarity': {
                'q_str':   ':DEC{a0}:SPI:SEL?',
                'set_str': ':DEC{a0}:SPI:SEL {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.OptionArgSpec(('ncs','cs')),
                ),
            },
            'decoder_spi_cs_polarity': {
                'q_str':   ':DEC{a0}:SPI:MODE?',
                'set_str': ':DEC{a0}:SPI:MODE {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.OptionArgSpec(('cs','timeout')),
                ),
            },
            'decoder_spi_timeout': {
                'q_str':   ':DEC{a0}:SPI:TIMeout?',
                'set_str': ':DEC{a0}:SPI:TIMeout {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.TypeArgSpec((int,float,)),
                ),
            },
            'decoder_spi_polarity': {
                'q_str':   ':DEC{a0}:SPI:POLarity?',
                'set_str': ':DEC{a0}:SPI:POLarity {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.neg_pos,
                ),
            },
            'decoder_spi_edge': {
                'q_str':   ':DEC{a0}:SPI:EDGE?',
                'set_str': ':DEC{a0}:SPI:EDGE {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.OptionArgSpec(('rise','fall')),
                ),
            },
            'decoder_spi_endian': {
                'q_str':   ':DEC{a0}:SPI:ENDian?',
                'set_str': ':DEC{a0}:SPI:ENDian {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.OptionArgSpec(('lsb','msb')),
                ),
            },
            'decoder_spi_width': {
                'q_str':   ':DEC{a0}:SPI:WIDTh?',
                'set_str': ':DEC{a0}:SPI:WIDTh {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.RangeArgSpec(8,32,int),
                ),
            },
        },
    },
    'decoder_parallel': {
    'name': 'Parallel Decoder Settings',
        'commands': {
            'decoder_parallel_clk': {
                'q_str':   ':DEC{a0}:PAR:CLK?',
                'set_str': ':DEC{a0}:PAR:CLK {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.decoder_source,
                ),
            },
            'decoder_parallel_source': {
                'q_str':   ':DEC{a0}:PAR:SOUR?',
                'set_str': ':DEC{a0}:PAR:SOUR {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.decoder_source,
                ),
            },
            'decoder_parallel_edge': {
                'q_str':   ':DEC{a0}:PAR:EDGE?',
                'set_str': ':DEC{a0}:PAR:EDGE {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.OptionArgSpec(('rise','fall','both')),
                ),
            },
            'decoder_parallel_width': {
                'q_str':   ':DEC{a0}:PAR:WIDTh?',
                'set_str': ':DEC{a0}:PAR:WIDTh {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.RangeArgSpec(1,16,int),
                ),
            },
            'decoder_parallel_bitsel': {
                'q_str':   ':DEC{a0}:PAR:BITX?',
                'set_str': ':DEC{a0}:PAR:BITX {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.RangeArgSpec(1,16,int),
                ),
            },
            'decoder_parallel_polarity': {
                'q_str':   ':DEC{a0}:PAR:POLarity?',
                'set_str': ':DEC{a0}:PAR:POLarity {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.neg_pos,
                ),
            },
            'decoder_parallel_noise_reject': {
                'q_str':   ':DEC{a0}:PAR:NREJect?',
                'set_str': ':DEC{a0}:PAR:NREJect {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.on_off,
                ),
            },
            'decoder_parallel_noise_reject_time': {
                'q_str':   ':DEC{a0}:PAR:NRTime?',
                'set_str': ':DEC{a0}:PAR:NRTime {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.RangeArgSpec(0,0.1,float),
                ),
            },
            'decoder_parallel_compensation_time': {
                'q_str':   ':DEC{a0}:PAR:CCOM?',
                'set_str': ':DEC{a0}:PAR:CCOM {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.RangeArgSpec(-0.1,0.1,float),
                ),
            },
            'decoder_parallel_plot': {
                'q_str':   ':DEC{a0}:PAR:PLOT?',
                'set_str': ':DEC{a0}:PAR:PLOT {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.on_off,
                ),
            },
        },
    },
}
