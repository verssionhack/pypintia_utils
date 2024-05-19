#!/bin/python3


import sys
import os
import os.path as op
from pintia import Pintia, ProblemType
from utils import parse_select_args
import json as j




def main():
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} <cookie_path>')
        exit(-1)


    api = Pintia(open(sys.argv[1], 'r').read())

    problem_sets = api.problem_sets(10).problem_sets
    for i in range(len(problem_sets)):
        p = problem_sets[i]
        print(f'[{i}] name={p.name} id={p.id} status={p.status}')
    selecteds = parse_select_args(input(f'Select 0-{len(problem_sets) - 1}? '))

    for selected in selecteds:
        p = problem_sets[selected]
        exams = api.problem_sets_exams(p.id)

        for problem in api.problem_sets_exam_list(p.id, exams.exam.id, ProblemType.PROGRAMMING.value, 0, 100).problem_set_problems:

            problem_detail = api.problem_sets_exam_problem(p.id, problem.id)
            print(f'{problem_detail.problem_set_problem.content}')


if __name__ == '__main__':
    main()
