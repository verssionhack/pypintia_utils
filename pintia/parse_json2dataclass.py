#!/bin/python3


import sys
import os
import os.path as op
from utils import json2dataclass
import json as j



def main():
    for arg in sys.argv[1:]:
        if ':' in arg:
            (path, name) = arg.split(':')
            name = op.basename(name)
        else:
            path, name = arg, op.basename(arg.rsplit('.', 1)[0])
        json = j.load(open(path, 'r'))
        dataclass_tb = json2dataclass(name, json)

        if not op.exists(name + '.py'):
            with open(name + '.py', 'w') as fd:
                fd.write('from dataclasses import dataclass\nfrom typing import *\n')
                for dataclass in dataclass_tb.values():
                    fd.write(dataclass)
                    fd.write('\n' * 4)
        else:
            print(f'skip parse {arg} since {name}.py exists')


if __name__ == '__main__':
    main()
