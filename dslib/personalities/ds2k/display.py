from ... import validator
from . import common_validators

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
                'validators': (
                    validator.TypeValidator((str,None)),
                ),
            },
            'disp_clear': {
                'cmd': ':DISP:CLEar',
            },
            'disp_type': {
                'base_str': ':DISP:TYPE',
                'validators': (
                    validator.OptionValidator(('vectors','dots')),
                ),
            },
            'disp_grading_time': {
                'base_str': ':DISP:GRAD:TIME',
                'validators': (
                    validator.OptionValidator(('min','inf','infinite',0.05,0.1,0.2,0.5,1,5,10,20),(str,float,int)),
                ),
            },
            'disp_wave_brightness': {
                'base_str': ':DISP:WBR',
                'validators': (
                    common_validators.is_percent,
                ),
            },
            'disp_grid_brightness': {
                'base_str': ':DISP:GBR',
                'validators': (
                    common_validators.is_percent,
                ),
            },
            'disp_menu_time': {
                'base_str': ':DISP:MPER',
                'validators': (
                    validator.OptionValidator((1,2,5,10,20,'infinite'),(str,float,int)),
                ),
            },
            'disp_grid': {
                'base_str': ':DISP:GRID',
                'validators': (
                    validator.OptionValidator(('full','half','none')),
                ),
            },
        },
    },
}

