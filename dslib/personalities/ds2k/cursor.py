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
            'cursor_mode': {
                'base_str': ':CURSor:MODE',
                'validators': (
                    ((str,), ('off','manual','track','auto','xy')),
                ),
            },
            'cursor_manual_type': {
                'base_str': ':CURSor:MANual:TYPE',
                'validators': (
                    ((str,), ('time','amplitude')),
                ),
            },
            'cursor_manual_source': {
                'base_str': ':CURSor:MANual:SOUR',
                'validators': (
                    ((str,), ('chan1','chan2','math','la','none')),
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
                    ((str,), ('percent','sunit')),
                ),
            },
            'cursor_manual_ax': {
                'base_str': ':CURSor:MANual:CAX',
                'validators': (
                    validators.cursor_pos_x,
                ),
            },
            'cursor_manual_bx': {
                'base_str': ':CURSor:MANual:CBX',
                'validators': (
                    validators.cursor_pos_x,
                ),
            },
            'cursor_manual_ay': {
                'base_str': ':CURSor:MANual:CAY',
                'validators': (
                    validators.cursor_pos_y,
                ),
            },
            'cursor_manual_bx': {
                'base_str': ':CURSor:MANual:CBY',
                'validators': (
                    validators.cursor_pos_y,
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
                'cmd': ':CURSor:TRACk:CAY?',
            },
            'cursor_track_by': {
                'cmd': ':CURSor:TRACk:CBY?',
            },
        },
        'simple_1_args': {
            'cursor_track_source1': {
                'base_str': ':CURSor:TRACk:SOURce1',
                'validators': (
                    ((str,), ('chan1','chan2','math','none')),
                ),
            },
            'cursor_track_source2': {
                'base_str': ':CURSor:TRACk:SOURce2',
                'validators': (
                    ((str,), ('chan1','chan2','math','none')),
                ),
            },
            'cursor_track_ax': {
                'base_str': ':CURSor:TRACk:CAX',
                'validators': (
                    validators.cursor_pos_x,
                ),
            },
            'cursor_track_bx': {
                'base_str': ':CURSor:TRACk:CBX',
                'validators': (
                validators.cursor_pos_x,
                ),
            },
        },
    },
}
