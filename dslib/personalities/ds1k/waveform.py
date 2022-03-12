from ... import argspec
from . import common_argspecs
import csv

def download_data(rs, args):
    channelstring = args[0]
    channels = []
    for c in channelstring.split(','):
        ic = int(c)
        if ic < 1 or ic > 4:
            raise Exception(f"Invalid channel identifier '{c}'; must be from 1 to 4")
        channels.append(ic)

    rs._cmdo("WAV:MODE NORM")
    outputs = []
    for chan in channels:
        rs._cmdo(f"WAV:SOUR CHAN{chan}")
        rs._cmdo("WAV:STAR 0")
        rs._cmdo("WAV:STOP 1200")
        rs._cmdo("WAV:FORM ASC")
        rs._cmdo(":WAV:DATA?")
        data = rs.slurpRigolBlob()
        data = data[0].decode('ascii')
        data = [float(d) for d in data.split(',')]
        outputs.append(data)

    if len(args) == 2:
        fn = args[1]
        with open(fn, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(channels)
            csvwriter.writerows(zip(*outputs))
            return f"Output written to {fn}"
    else:
        return {channels[i]: outputs[i] for i in range(len(channels))}

CONFIG = {
    'waveform': {
        'name': 'Waveforms',
        'commands': {
            'download_data': {
                'func': download_data,
                'help': 'Download data from one or more channels as CSV, specified as "1,2,4[:out.csv]"',
                'argspecs': (
                    argspec.RegexArgSpec(pattern=r'^([1234])(,\s*[1234]+)*$'),
                    argspec.TypeArgSpec((str,None)),
                )
            },
        },
    },
}
