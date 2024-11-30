from pintia.utils import parse_cookie
import json as j
from random import randint
import os

def format_c_code(text: str):
    filepath = '/tmp/' + random_chars(20)
    with open(filepath, 'w') as fd:
        fd.write(text)
    

    if not os.path.exists('/bin/indent'):
        os.system('./install_denpendcies.sh')

    os.system(f'indent -nbad -bap -nbc -bbo -hnl -br -brs -c33 -cd33 -ncdb -ce -ci4 -cli0 -d0 -di1 -nfc1 -i4 -ip0 -lp -npcs -nprs -npsl -sai -saf -saw -ncs -nsc -sob -nfca -cp33 -ss -ts4 -il1 -brf -nut {filepath}')

    return open(filepath, 'r').read()




def parse_select_args(args_txt: str):
    selecteds = []
    for i in args_txt.replace(' ', '').split(','):
        if i.isdigit():
            selecteds.append(int(i))
        elif len(i.split('-')) == 2:
            (a, b) = i.split('-')
            if a.isdigit() and b.isdigit():
                selecteds.extend(range(int(a), int(b) + 1))
    return list(set(selecteds))


def load_cookie(path):
    content = open(path, 'r').read()
    try:
        return j.loads(content)
    except:
        return parse_cookie(content)


def random_chars(count: int):
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    ret = ''
    for _ in range(count):
        ret += chars[randint(0, len(chars) - 1)]
    return ret
