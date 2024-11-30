#!/bin/python3



import json as j
import os
from sys import argv
import os.path as op


if __name__ == '__main__':

    if len(argv) < 3:
        print(f'Usage: {argv[0]} [import] [export_dir]')
        exit()

    
    import_content = j.load(open(argv[1], 'r'))
    export_dir = argv[2]

    if not op.exists(export_dir):
        os.makedirs(export_dir)

    for sid, sv in import_content.items():
        for pid, pv in sv.items():
            export_sdir = op.join(export_dir, sid)
            if not op.exists(export_sdir):
                os.makedirs(export_sdir)

            open(op.join(export_sdir, pv['title']), 'w').write(pv['program_content'])
