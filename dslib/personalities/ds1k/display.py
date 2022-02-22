from ... import validator
from . import common_validators

def screenCap(rs, args):
    alen = len(args)
    fn = None
    color = 'on' 
    invert = 'off'
    fmt = 'png'
    if alen > 0:
        fn = args[0]
    if alen > 1:
        color = 'off' if args[1] == 'bw' else 'on'
    if alen > 2:
        invert = 'on' if args[2] == 'invert' else 'off'
    if alen > 3:
        fmt = args[3]
    
    if fn is None or not len(fn):
        now = rs.fileSafeDate()
        fn = f'rigol_cap_{now}.{fmt}'
    rs._cmdo(f':DISPLAY:DATA? {color},{invert},{fmt}')
    inner, whole = rs.slurpRigolBlob()
    with open(fn,'wb') as ofh:
        ofh.write(inner)
    return fn


CONFIG = {
    'display': {
        'name': 'Display',
        'real_functions': {
            'capture': {
                'func': screenCap,
                'help': 'Save an image to disk exactly as it appears on sreen, in color or bw, or with the colors inverted',
                'validators': (
                    validator.TypeValidator((str,None)),
                    validator.OptionValidator(('color','bw')),
                    validator.OptionValidator(('invert','normal')),
                    validator.OptionValidator(('bmp8','bmp24','png','jpeg','tiff')),
                )
            }
        },
        'simple_1_args': {
            'disp_type': {
                'help': 'Show traces as vector of connected lines or just dots',
                'base_str': ':DISP:TYPE',
                'validators': (
                    validator.OptionValidator(('vectors','dots')),
                ),
            },
            'disp_grading_time': {
                'help': 'Time to fade out intensity-graded trace',
                'base_str': ':DISP:GRAD:TIME',
                'validators': (
                    validator.OptionValidator(('min','inf','infinite',0.1,0.2,0.5,1,5,10),(str,float,int)),
                ),
            },
            'disp_wave_brightness': {
                'help': 'percent brightness for trace',
                'base_str': ':DISP:WBR',
                'validators': (
                    common_validators.is_percent,
                ),
            },
            'disp_grid_brightness': {
                'help': 'percent brightness for graticule',
                'base_str': ':DISP:GBR',
                'validators': (
                    common_validators.is_percent,
                ),
            },
            'disp_grid': {
                'help': 'show full, partial, or no graticule',
                'base_str': ':DISP:GRID',
                'validators': (
                    validator.OptionValidator(('full','half','none')),
                ),
            },
        },
    },
}

