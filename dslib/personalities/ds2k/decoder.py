from ... import argspec
from . import common_argspecs

CONFIG = {
    'decoder': {
        'name': 'Decoder Shared',
        'commands': {
            'decoder_table_export': {
                'set_str': ':BUS{a0}:MODE {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                ),
            },
            'decoder_mode': {
                'q_str':   ':BUS{a0}:MODE?',
                'set_str': ':BUS{a0}:MODE {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.OptionArgSpec(('parallel','rs232','spi','iic','can')),
                ),
            },
            'decoder_display': {
                'q_str':   ':BUS{a0}:DISP?',
                'set_str': ':BUS{a0}:DISP {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.on_off,
                ),
            },
            'decoder_format': {
                'q_str':   ':BUS{a0}:FORM?',
                'set_str': ':BUS{a0}:FORM {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.OptionArgSpec(('hex','ascii','dec','bin')),
                ),
            },
            'decoder_event_table': {
                'q_str':   ':BUS{a0}:EVEN?',
                'set_str': ':BUS{a0}:EVEN {a1}',
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
                'q_str':   ':BUS{a0}:RS232:TX?',
                'set_str': ':BUS{a0}:RS232:TX {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.decoder_source,
                ),
            },
            'decoder_uart_rx_source': {
                'q_str':   ':BUS{a0}:RS232:RX?',
                'set_str': ':BUS{a0}:RS232:RX {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.decoder_source,
                ),
            },
            'decoder_uart_polarity': {
                'q_str':   ':BUS{a0}:RS232:POL?',
                'set_str': ':BUS{a0}:RS232:POL {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.neg_pos,
                ),
            },
            'decoder_uart_endian': {
                'q_str':   ':BUS{a0}:RS232:END?',
                'set_str': ':BUS{a0}:RS3232:END {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.OptionArgSpec(('lsb','msb')),
                ),
            },
            'decoder_uart_baud': {
                'q_str':   ':BUS{a0}:RS232:BAUD?',
                'set_str': ':BUS{a0}:RS232:BAUD {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.OptionArgSpec(
                        ('2400','4800','9600','19200','38400','57600',
                         '115200','23040','92160','1000000','user')
                    ),
                ),
            },
            'decoder_uart_baud': {
                'q_str':   ':BUS{a0}:RS232:BUSer?',
                'set_str': ':BUS{a0}:RS232:BUSer {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.RangeArgSpec(110,2000000,int),
                ),
            },
            'decoder_uart_width': {
                'q_str':   ':BUS{a0}:RS232:DBIT?',
                'set_str': ':BUS{a0}:RS232:DBIT {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.RangeArgSpec(5,8,int),
                ),
            },
            'decoder_uart_stop': {
                'q_str':   ':BUS{a0}:RS232:STOP?',
                'set_str': ':BUS{a0}:RS232:STOP {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.OptionArgSpec((1,1.5,2),(int,float)),
                ),
            },
            'decoder_uart_parity': {
                'q_str':   ':BUS{a0}:RS232:PARity?',
                'set_str': ':BUS{a0}:RS232:PARity {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.OptionArgSpec(('none','even','odd')),
                ),
            },
            'decoder_uart_packet': {
                'q_str':   ':BUS{a0}:RS232:PACK?',
                'set_str': ':BUS{a0}:RS232:PACK {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.on_off,
                ),
            },
            'decoder_uart_tx_thresh': {
                'q_str':   ':BUS{a0}:RS232:TTHR?',
                'set_str': ':BUS{a0}:RS232:TTHR {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.TypeArgSpec(float),
                ),
            },
            'decoder_uart_rx_thresh': {
                'q_str':   ':BUS{a0}:RS232:RTHR?',
                'set_str': ':BUS{a0}:RS232:RTHR {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.TypeArgSpec(float),
                ),
            },
            'decoder_uart_offset': {
                'q_str':   ':BUS{a0}:RS232:OFFS?',
                'set_str': ':BUS{a0}:RS232:OFFS {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.offset_pos,
                ),
            },
        },
    },
    'decoder_iic': {
        'name': 'Decoder I2C Settings',
        'commands': {
            'decoder_iic_scl': {
                'q_str':   ':BUS{a0}:IIC:SCLK:SOUR?',
                'set_str': ':BUS{a0}:IIC:SCLK:SOUR {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.decoder_source,
                ),
            },
            'decoder_iic_scl_threshold': {
                'q_str':   ':BUS{a0}:IIC:SCLK:THR?',
                'set_str': ':BUS{a0}:IIC:SCLK:THR {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.TypeArgSpec(float),
                ),
            },
            'decoder_iic_sda': {
                'q_str':   ':BUS{a0}:IIC:SDA:SOUR?',
                'set_str': ':BUS{a0}:IIC:SDA:SOUR {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.decoder_source,
                ),
            },
            'decoder_iic_sda_threshold': {
                'q_str':   ':BUS{a0}:IIC:SDA:THR?',
                'set_str': ':BUS{a0}:IIC:SDA:THR {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.TypeArgSpec(float),
                ),
            },
            'decoder_iic_offset': {
                'q_str':   ':BUS{a0}:IIC:OFFS?',
                'set_str': ':BUS{a0}:IIC:OFFS {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.offset_pos,
                ),
            },
        },
    },
    'decoder_spi': {
        'name': 'Decoder SPI Settings',
        'commands': {
            'decoder_spi_mclk': {
                'q_str':   ':BUS{a0}:SPI:SCLK:SOUR?',
                'set_str': ':BUS{a0}:SPI:SCLK:SOUR {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.decoder_source,
                ),
            },
            'decoder_spi_mclk_slope': {
                'q_str':   ':BUS{a0}:SPI:SCLK:SLOP?',
                'set_str': ':BUS{a0}:SPI:SCLK:SLOP {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.neg_pos,
                ),
            },
            'decoder_spi_mclk_threshold': {
                'q_str':   ':BUS{a0}:SPI:SCLK:THRe?',
                'set_str': ':BUS{a0}:SPI:SCLK:THRe {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.TypeArgSpec(float),
                ),
            },
            'decoder_spi_ss': {
                'q_str':   ':BUS{a0}:SPI:SS:SOUR?',
                'set_str': ':BUS{a0}:SPI:SS:SOUR {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.decoder_source,
                ),
            },
            'decoder_spi_ss_polarity': {
                'q_str':   ':BUS{a0}:SPI:SS:POL?',
                'set_str': ':BUS{a0}:SPI:SS:POL{a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.neg_pos,
                ),
            },
            'decoder_spi_ss_threshold': {
                'q_str':   ':BUS{a0}:SPI:SS:THRe?',
                'set_str': ':BUS{a0}:SPI:SS:THRe {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.TypeArgSpec(float),
                ),
            },
            'decoder_spi_miso': {
                'q_str':   ':BUS{a0}:SPI:SDA:SOUR?',
                'set_str': ':BUS{a0}:SPI:SDA:SOUR {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.decoder_source,
                ),
            },
            'decoder_spi_miso_polarity': {
                'q_str':   ':BUS{a0}:SPI:SDA:POL?',
                'set_str': ':BUS{a0}:SPI:SDA:POL {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.high_low,
                ),
            },
            'decoder_spi_miso_threshold': {
                'q_str':   ':BUS{a0}:SPI:SDA:THRe?',
                'set_str': ':BUS{a0}:SPI:SDA:THRe {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.TypeArgSpec(float),
                ),
            },
            'decoder_spi_width': {
                'q_str':   ':BUS{a0}:SPI:DBIT?',
                'set_str': ':BUS{a0}:SPI:DBIT {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.RangeArgSpec(4,32,int),
                ),
            },
            'decoder_spi_endian': {
                'q_str':   ':BUS{a0}:SPI:END?',
                'set_str': ':BUS{a0}:SPI:END {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.OptionArgSpec(('msb','lsb')),
                ),
            },
            'decoder_spi_offset': {
                'q_str':   ':BUS{a0}:SPI:END?',
                'set_str': ':BUS{a0}:SPI:END {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.offset_pos,
                ),
            },
            'decoder_spi_mode': {
                'q_str':   ':BUS{a0}:SPI:MODE?',
                'set_str': ':BUS{a0}:SPI:MODE {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.OptionArgSpec(('cs','timeout')),
                ),
            },
            'decoder_spi_mode': {
                'q_str':   ':BUS{a0}:SPI:TIM:TIME?',
                'set_str': ':BUS{a0}:SPI:TIM:TIME {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.RangeArgSpec(100e-09,1,float),
                ),
            },
        },
    },
    'decoder_parallel': {
    'name': 'Parallel Decoder Settings',
        'commands': {
            'decoder_parallel_clk': {
                'q_str':   ':BUS{a0}:PAR:CLK?',
                'set_str': ':BUS{a0}:PAR:CLK {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.decoder_source,
                ),
            },
            'decoder_parallel_slope': {
                'q_str':   ':BUS{a0}:PAR:SLOP?',
                'set_str': ':BUS{a0}:PAR:SLOP {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.neg_pos_both,
                ),
            },
            'decoder_parallel_bitsel': {
                'q_str':   ':BUS{a0}:PAR:BSET?',
                'set_str': ':BUS{a0}:PAR:BSET {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.decoder_source,
                    # TODO: handle more than one bit!
                ),
            },
            'decoder_parallel_threshold': {
                'q_str':   ':BUS{a0}:PAR:THR? {a1}',
                'set_str': ':BUS{a0}:PAR:THR {a1} {a2}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.decoder_source,
                    argspec.TypeArgSpec((float,int)),
                ),
            },
            'decoder_parallel_offset': {
                'q_str':   ':BUS{a0}:PAR:OFF?',
                'set_str': ':BUS{a0}:PAR:OFF {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.decoder_source,
                    # this range should be different in normal, stats,
                    # or half-screen mode
                    common_argspecs.offset_pos,
                ),
            },
        },
    },
    'decoder_can': {
    'name': 'CAN Decoder Settings',
        'commands': {
            'decoder_can_source': {
                'q_str':   ':BUS{a0}:CAN:SOUR?',
                'set_str': ':BUS{a0}:CAN:SOUR {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.decoder_source,
                ),
            },
            'decoder_can_type': {
                'q_str':   ':BUS{a0}:CAN:STYP?',
                'set_str': ':BUS{a0}:CAN:STYP {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.OptionArgSpec(('tx','rx','canh','canl','differential')),
                ),
            },
            'decoder_can_baud': {
                'q_str':   ':BUS{a0}:CAN:BAUD?',
                'set_str': ':BUS{a0}:CAN:BAUD {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.OptionArgSpec(
                        ('2400','4800','9600','19200','38400','57600',
                         '115200','23040','92160','1000000','user')
                    ),
                ),
            },
            'decoder_can_user_baud': {
                'q_str':   ':BUS{a0}:CAN:BUSer?',
                'set_str': ':BUS{a0}:CAN:BUSer {a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.RangeArgSpec(10000,1000000,int),
                ),
            },
            'decoder_can_threshold': {
                'q_str':   ':BUS{a0}:CAN:THR?',
                'set_str': ':BUS{a0}:CAN:THR{a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    argspec.TypeArgSpec(float),
                ),
            },
            'decoder_can_threshold': {
                'q_str':   ':BUS{a0}:CAN:THR?',
                'set_str': ':BUS{a0}:CAN:THR{a1}',
                'argspecs': (
                    common_argspecs.decoder_number,
                    common_argspecs.offset_pos,
                ),
            },
        },
    },
}
