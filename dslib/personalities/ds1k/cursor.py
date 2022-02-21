from . import validators

CONFIG = {
    'cursor_man': {
        'name': 'Manual Cursor',
        'simple_0_args': {
            'cursor_manual_ax_val': {
                'cmd': ':CURSor:MANual:AXValue?',
            },
            'cursor_manual_bx_val': {
                'cmd': ':CURSor:MANual:BXValue?',
            },
            'cursor_manual_ay_val': {
                'cmd': ':CURSor:MANual:AYValue?',
            },
            'cursor_manual_by_val': {
                'cmd': ':CURSor:MANual:BYValue?',
            },
            'cursor_manual_x_delta': {
                'cmd': ':CURSor:MANual:XDELta?',
            },
            'cursor_manual_x_delta_inv': {
                'cmd': ':CURSor:MANual:IXDELta?',
            },
            'cursor_manual_y_delta': {
                'cmd': ':CURSor:MANual:YDELta?',
            },
        },
        'simple_1_args': {
            'cursor_manual_type': {
                'base_str': ':CURSor:MANual:TYPE',
                'validators': (
                    ((str,), ('x','y')),
                ),
            },
            'cursor_manual_source': {
                'base_str': ':CURSor:MANual:SOUR',
                'validators': (
                    ((str,), ('chan1','chan2','chan3','chan4','math','la')),
                ),
            },
            'cursor_manual_time_unit': {
                'base_str': ':CURSor:MANual:TUN',
                'validators': (
                    ((str,), ('s','hz','degree','percent')),
                ),
            },
            'cursor_manual_vertical_unit': {
                'base_str': ':CURSor:MANual:VUN',
                'validators': (
                    ((str,), ('percent','source')),
                ),
            },
            'cursor_manual_ax': {
                'base_str': ':CURSor:MANual:AX',
                'validators': (
                    validators.cursor_pos,
                ),
            },
            'cursor_manual_bx': {
                'base_str': ':CURSor:MANual:BX',
                'validators': (
                    validators.cursor_pos,
                ),
            },
            'cursor_manual_ay': {
                'base_str': ':CURSor:MANual:AY',
                'validators': (
                    validators.cursor_pos,
                ),
            },
            'cursor_manual_bx': {
                'base_str': ':CURSor:MANual:BY',
                'validators': (
                    validators.cursor_pos,
                ),
            },
        },
    },
    'cursor_track': {
        'name': 'Tracking Cursor',
        'simple_0_args': {
            'cursor_track_ax_val': {
                'cmd': ':CURSor:TRACk:AXValue?',
            },
            'cursor_track_ay_val': {
                'cmd': ':CURSor:TACKk:AYValue?',
            },
            'cursor_track_bx_val': {
                'cmd': ':CURSor:TRACk:BXValue?',
            },
            'cursor_track_by_val': {
                'cmd': ':CURSor:TRACk:BYValue?',
            },
            'cursor_track_x_delta': {
                'cmd': ':CURSor:TRACk:XDELta?',
            },
            'cursor_track_x_delta_inv': {
                'cmd': ':CURSor:TRACk:IXDELta?',
            },
            'cursor_track_y_delta': {
                'cmd': ':CURSor:TRACk:YDELta?',
            },
            'cursor_track_ay': {
                'cmd': ':CURSor:TRACk:AY?',
            },
            'cursor_track_by': {
                'cmd': ':CURSor:TRACk:BY?',
            },
        },
        'simple_1_args': {
            'cursor_track_source1': {
                'base_str': ':CURSor:TRACk:SOURce1',
                'validators': (
                    ((str,), ('off', 'chan1','chan2','chan3','chan4','math')),
                ),
            },
            'cursor_track_source2': {
                'base_str': ':CURSor:TRACk:SOURce2',
                'validators': (
                    ((str,), ('off','chan1','chan2','chan3','chan4','math')),
                ),
            },
            'cursor_track_ax': {
                'base_str': ':CURSor:TRACk:AX',
                'validators': (
                    validators.cursor_pos,
                ),
            },
            'cursor_track_bx': {
                'base_str': ':CURSor:TRACk:BX',
                'validators': (
                validators.cursor_pos,
                ),
            },
        },
    },
    'cursor_auto': {
        'name': 'Automatic Cursor',
        'simple_0_args': {
            'cursor_auto_ax_val': {
                'cmd': ':CURSor:AUTO:AXValue?',
            },
            'cursor_auto_ay_val': {
                'cmd': ':CURSor:AUTO:AYValue?',
            },
            'cursor_auto_bx_val': {
                'cmd': ':CURSor:AUTO:BXValue?',
            },
            'cursor_auto_by_val': {
                'cmd': ':CURSor:AUTO:BYValue?',
            },
            'cursor_auto_ax': {
                'cmd': ':CURSor:AUTO:AX?',
            },
            'cursor_auto_ay': {
                'cmd': ':CURSor:AUTO:AY?',
            },
            'cursor_auto_bx': {
                'cmd': ':CURSor:AUTO:BX?',
            },
            'cursor_auto_by': {
                'cmd': ':CURSor:AUTO:BY?',
            },
        }
    },
    'cursor_xymode': {
        'name': 'XY Mode Cursor',
        'simple_0_args': {
            'cursor_xy_ax_val': {
                'cmd': ':CURSor:XY:AXValue?',
            },
            'cursor_xy_ay_val': {
                'cmd': ':CURSor:XY:AYValue?',
            },
            'cursor_xy_bx_val': {
                'cmd': ':CURSor:XY:BXValue?',
            },
            'cursor_xy_by_val': {
                'cmd': ':CURSor:XY:BYValue?',
            },
        },
        'simple_1_args': {
            'cursor_xy_ax': {
                'base_str': ':CURSor:XY:AX',
                'validators': (
                    validators.cursor_pos,
                ),
            },
            'cursor_xy_ay': {
                'base_str': ':CURSor:XY:AY',
                'validators': (
                    validators.cursor_pos,
                ),
            },
            'cursor_xy_bx': {
                'base_str': ':CURSor:XY:BX',
                'validators': (
                    validators.cursor_pos,
                ),
            },
            'cursor_xy_by': {
                'base_str': ':CURSor:XY:BY',
                'validators': (
                    validators.cursor_pos,
                ),
            },
        }
    },
}
