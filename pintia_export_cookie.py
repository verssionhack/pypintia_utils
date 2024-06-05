#!/bin/python3


import sys
import os
import os.path as op
from pintia import Pintia
from getpass import getpass
from utils import random_chars
import json as j

def main():

    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} <save_path>')
        exit(-1)

    api = Pintia()
    phone = '+86' + input('Phone: +86')
    password = getpass()
    api.login(phone, password)

    export_s = j.dumps(dict(api.session.cookies))


    try:
        open(sys.argv[1], 'w').write(export_s)
    except Exception as e:
        print('Error {e}')
        output_path = random_chars(10) + f'.cookie'
        print(f'Export to {output_path}')
        open(output_path, 'w').write(export_s)


if __name__ == '__main__':
    main()
