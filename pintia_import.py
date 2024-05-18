#!/bin/python3


import sys
import os
import os.path as op
from pintia import Pintia
import json as j
from pintia.problem_sets import ProblemSetsItem
from pintia.problem_status import ProblemStatus
from utils import load_cookie

def main():
    if len(sys.argv) < 3:
        print(f'Usage: {sys.argv[0]} <cookies> <load_path>')
        exit(-1)

    _load = j.load(open(sys.argv[2], 'r'))

    api = Pintia(load_cookie(sys.argv[1]))
    problem_sets = [i for i in api.problem_sets(10).problem_sets if i.id in _load]

    for i in range(len(problem_sets)):
        p = problem_sets[i]
        print(f'[{i}] name={p.name} id={p.id} status={p.status}')

    selecteds = [int(i) for i in input(f'Select 0-{len(problem_sets) - 1}? ').split('-') if i.isdigit()]
    for selected in selecteds:
        p = problem_sets[selected]
        _load_problems = _load[p.id]
        exam_status = api.problem_sets_status(p.id)
        for problem in exam_status.problem_status:
            if problem.problem_submission_status != 'PROBLEM_ACCEPTED' and problem.id in _load_problems:
                print(f'Submit {p.name}:{problem.id}')
                api.problem_sets_exam_problem_submission(**_load_problems[problem.id])


if __name__ == '__main__':
    main()
