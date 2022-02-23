from ... import argspec
from . import common_argspecs

CONFIG = {
    'cursor_man': {
        'name': 'Manual Cursor',
        'commands': {
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
            'cursor_manual_type': {
                'base_str': ':CURSor:MANual:TYPE',
                'argspecs': (
                    argspec.OptionArgSpec(('x','y')),
                ),
            },
            'cursor_manual_source': {
                'base_str': ':CURSor:MANual:SOUR',
                'argspecs': (
                    argspec.OptionArgSpec(('chan1','chan2','chan3','chan4','math','la')),
                ),
            },
            'cursor_manual_time_unit': {
                'base_str': ':CURSor:MANual:TUN',
                'argspecs': (
                    argspec.OptionArgSpec(('s','hz','degree','percent')),
                ),
            },
            'cursor_manual_vertical_unit': {
                'base_str': ':CURSor:MANual:VUN',
                'argspecs': (
                    argspec.OptionArgSpec(('percent','source')),
                ),
            },
            'cursor_manual_ax': {
                'base_str': ':CURSor:MANual:AX',
                'argspecs': (
                    common_argspecs.cursor_pos,
                ),
            },
            'cursor_manual_bx': {
                'base_str': ':CURSor:MANual:BX',
                'argspecs': (
                    common_argspecs.cursor_pos,
                ),
            },
            'cursor_manual_ay': {
                'base_str': ':CURSor:MANual:AY',
                'argspecs': (
                    common_argspecs.cursor_pos,
                ),
            },
            'cursor_manual_bx': {
                'base_str': ':CURSor:MANual:BY',
                'argspecs': (
                    common_argspecs.cursor_pos,
                ),
            },
        },
    },
    'cursor_track': {
        'name': 'Tracking Cursor',
        'commnds': {
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
            'cursor_track_source1': {
                'base_str': ':CURSor:TRACk:SOURce1',
                'argspecs': (
                    argspec.OptionArgSpec(('off', 'chan1','chan2','chan3','chan4','math')),
                ),
            },
            'cursor_track_source2': {
                'base_str': ':CURSor:TRACk:SOURce2',
                'argspecs': (
                    argspec.OptionArgSpec(('off','chan1','chan2','chan3','chan4','math')),
                ),
            },
            'cursor_track_ax': {
                'base_str': ':CURSor:TRACk:AX',
                'argspecs': (
                    common_argspecs.cursor_pos,
                ),
            },
            'cursor_track_bx': {
                'base_str': ':CURSor:TRACk:BX',
                'argspecs': (
                common_argspecs.cursor_pos,
                ),
            },
        },
    },
    'cursor_auto': {
        'name': 'Automatic Cursor',
        'commands': {
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
        'commands': {
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
            'cursor_xy_ax': {
                'base_str': ':CURSor:XY:AX',
                'argspecs': (
                    common_argspecs.cursor_pos,
                ),
            },
            'cursor_xy_ay': {
                'base_str': ':CURSor:XY:AY',
                'argspecs': (
                    common_argspecs.cursor_pos,
                ),
            },
            'cursor_xy_bx': {
                'base_str': ':CURSor:XY:BX',
                'argspecs': (
                    common_argspecs.cursor_pos,
                ),
            },
            'cursor_xy_by': {
                'base_str': ':CURSor:XY:BY',
                'argspecs': (
                    common_argspecs.cursor_pos,
                ),
            },
        }
    },
}
