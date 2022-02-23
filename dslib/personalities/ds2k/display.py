from ... import argspec
from . import common_argspecs

def screenCap(rs, args):
    alen = len(args)
    fn = None
    if alen > 0:
        fn = args[0]
    if fn is None or not len(fn):
        now = rs.fileSafeDate()
        fn = f'rigol_cap_{now}.bmp'
    rs._cmdo(f':DISPLAY:DATA?')
    inner, whole = rs.slurpRigolBlob()
    with open(fn,'wb') as ofh:
        ofh.write(inner)
    return fn


CONFIG = {
    'display': {
        'name': 'Display',
        'commands': {
            'capture': {
                'func': screenCap,
                'argspecs': (
                    argspec.TypeArgSpec((str,None)),
                ),
            },
            'disp_clear': {
                'cmd': ':DISP:CLEar',
            },
            'disp_type': {
                'base_str': ':DISP:TYPE',
                'argspecs': (
                    argspec.OptionArgSpec(('vectors','dots')),
                ),
            },
            'disp_grading_time': {
                'base_str': ':DISP:GRAD:TIME',
                'argspecs': (
                    argspec.OptionArgSpec(('min','inf','infinite',0.05,0.1,0.2,0.5,1,5,10,20),(str,float,int)),
                ),
            },
            'disp_wave_brightness': {
                'base_str': ':DISP:WBR',
                'argspecs': (
                    common_argspecs.is_percent,
                ),
            },
            'disp_grid_brightness': {
                'base_str': ':DISP:GBR',
                'argspecs': (
                    common_argspecs.is_percent,
                ),
            },
            'disp_menu_time': {
                'base_str': ':DISP:MPER',
                'argspecs': (
                    argspec.OptionArgSpec((1,2,5,10,20,'infinite'),(str,float,int)),
                ),
            },
            'disp_grid': {
                'base_str': ':DISP:GRID',
                'argspecs': (
                    argspec.OptionArgSpec(('full','half','none')),
                ),
            },
        },
    },
}

