#!/bin/python3


import sys
import os
import os.path as op
from pintia import Pintia
import json as j




def main():
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} <cookies>.json')
        exit(-1)

    cookies = j.load(open(sys.argv[1], 'r'))

    api = Pintia(cookies)

    for p in api.problem_sets(10).problem_sets:
        print(api.problem_sets_exams(p.id))


if __name__ == '__main__':
    main()
