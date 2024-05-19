import json as j


def json2dataclass(name, data: dict) -> dict:
    table = {}
    dataclass_s = \
f'''@dataclass
class {snake2pascal(name)}:\n'''

    dataclass_init = \
f'''\n    def __init__(self, data: dict):\n        if data == None:\n            return None'''
    if len(data.values()) == 0:
        dataclass_init += \
f"""\n        pass"""
    else:
        for k, v in data.items():
            list_parse = False
            if type(v) == type(''):
                dataclass_s += '    ' + pascal2snake(k) + ': str\n'
            elif type(v) == type(0):
                dataclass_s += '    ' + pascal2snake(k) + ': int\n'
            elif type(v) == type(0.0):
                dataclass_s += '    ' + pascal2snake(k) + ': float\n'
            elif type(v) == type(True):
                dataclass_s += '    ' + pascal2snake(k) + ': bool\n'
            elif type(v) == type({}):
                dataclass_s += '    ' + pascal2snake(k) + ': ' + snake2pascal(k) + '\n'
                table.update(json2dataclass(k, v))
            elif type(v) == type([]):
                if len(v) == 0:
                    dataclass_s += '    ' + pascal2snake(k) + ': list\n'
                    dataclass_init += \
        f"""\n        self.{pascal2snake(k)} = data.get('{pascal2snake(k)}')"""
                    continue
                tp = type(v[0])
                all_eq = True
                for i in v:
                    if type(i) != tp:
                        all_eq = False
                        break
                if not all_eq:
                    dataclass_s += '    ' + pascal2snake(k) + ': list\n'
                elif tp == type({}):
                    f_imp = str(json2dataclass('ArrayFirst', v[0]))
                    all_eq = True
                    for i in v:
                        if f_imp != str(json2dataclass('ArrayFirst', i)):
                            all_eq = False
                            break
                    if not all_eq:
                        dataclass_s += '    ' + pascal2snake(k) + ': list\n'
                    else:
                        list_parse = True
                        datac_name = snake2pascal(k + '_item')

                        table.update(json2dataclass(datac_name, v[0]))

                        dataclass_s += '    ' + pascal2snake(k) + f': List[{datac_name}]\n'
                        dataclass_init += \
            f"""\n        self.{pascal2snake(k)} = [{snake2pascal(k)}Item(i) for i in (data.get('{pascal2snake(k)}') if data.get('{pascal2snake(k)}') != None else [])]"""
                else:
                    if type(v[0]) == type(''):
                        dataclass_s += '    ' + pascal2snake(k) + ': List[str]\n'
                    elif type(v[0]) == type(0):
                        dataclass_s += '    ' + pascal2snake(k) + ': List[int]\n'
                    elif type(v[0]) == type(0.0):
                        dataclass_s += '    ' + pascal2snake(k) + ': List[float]\n'
                    elif type(v[0]) == type(True):
                        dataclass_s += '    ' + pascal2snake(k) + ': List[bool]\n'
                    elif type(v[0]) == type([]):
                        dataclass_s += '    ' + pascal2snake(k) + ': List[list]\n'

            if not list_parse:
                if table.get(snake2pascal(k)):
                    dataclass_init += \
        f"""\n        self.{pascal2snake(k)} = {snake2pascal(k)}(data.get('{pascal2snake(k)}'))"""
                else:
                    dataclass_init += \
        f"""\n        self.{pascal2snake(k)} = data.get('{pascal2snake(k)}')"""

    dataclass_s += '\n\n\n' + dataclass_init
    table[snake2pascal(name)] = dataclass_s
    return table


def pascal2snake(value: str) -> str:
    if value.isupper():
        return value.lower()
    ret = ''
    for c in value:
        if 'A' <= c <= 'Z':
            if len(ret) > 0:
                ret += '_'
            ret += c.lower()
        else:
            ret += c
    return ret

def snake2pascal(value: str) -> str:
    ret = ''
    upper=True
    for c in value:
        if c == '_':
            upper = True
        else:
            if upper:
                upper = False
                ret += c.upper()
            else:
                ret += c
    return ret

def dict_key2snake_name(data: dict):
    if type(data) == type({}):
        keys = list(data.keys())
        for key in keys:
            dict_key2snake_name(data[key])
            if type(data[key]) == type([]):
                for i in range(len(data[key])):
                    dict_key2snake_name(data[key][i])

            data[pascal2snake(key)] = data.pop(key)


def parse_cookie(data: str):
    cookies = {}
    if len(data) == 0:
        return cookies
    data = data.replace('\n', '').split(';')
    for ktvs in data:
        if not '=' in ktvs:
            continue
        ktv = ktvs.split('=')
        ktv[0] = ktv[0].strip().rstrip()
        ktv[1] = ktv[1].strip().rstrip()
        cookies[ktv[0]] = ktv[1]
    return cookies
