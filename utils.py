from pintia.utils import parse_cookie
import json as j

def load_cookie(path):
    content = open(path, 'r').read()
    try:
        return j.load(content)
    except:
        return parse_cookie(content)

