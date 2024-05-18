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
        print(f'Usage: {sys.argv[0]} <cookies> <save_path>')
        exit(-1)

    api = Pintia(load_cookie(sys.argv[1]))
    problem_sets = api.problem_sets(10).problem_sets
    for i in range(len(problem_sets)):
        p = problem_sets[i]
        print(f'[{i}] name={p.name} id={p.id} status={p.status}')
    selecteds = [int(i) for i in input(f'Select 0-{len(problem_sets) - 1}? ').split('-') if i.isdigit()]
    export = {}
    for selected in selecteds:
        p = problem_sets[selected]
        export[p.id] = {}
        exam_status = api.problem_sets_status(p.id)
        for problem in exam_status.problem_status:
            if problem.problem_submission_status == 'PROBLEM_ACCEPTED':
                if problem.problem_type == 'CODE_COMPLETION':
                    last_submission = api.problem_sets_exam_problem_last_submissions(p.id, problem.id)
                    export[p.id][problem.id] = {
                            'problem_sets_id': p.id,
                            'exam_problem_id': problem.id,
                            'compiler': last_submission.submission.compiler,
                            'program_content': last_submission.submission.submission_details[-1].code_completion_submission_detail.program,
                            'problem_type': last_submission.submission.problem_type,
                            }
                    #print(api.problem_sets_exam_problem_last_submissions(p.id, problem.id).submission.submission_details[-1].code_completion_submission_detail.program)
                if problem.problem_type == 'PROGRAMMING':
                    last_submission = api.problem_sets_exam_problem_last_submissions(p.id, problem.id)
                    export[p.id][problem.id] = {
                            'problem_sets_id': p.id,
                            'exam_problem_id': problem.id,
                            'compiler': last_submission.submission.compiler,
                            'program_content': last_submission.submission.submission_details[-1].programming_submission_detail.program,
                            'problem_type': last_submission.submission.problem_type,
                            }
                    #print(api.problem_sets_exam_problem_last_submissions(p.id, problem.id).submission.submission_details[-1].programming_submission_detail.program)
    export_s = j.dumps(export)

    try:
        open(sys.argv[2], 'w').write(export_s)
    except Exception as e:
        print('Error {e}')
        output_path = f'{p.name}.json'
        print(f'Reexport to {output_path}')
        open(output_path, 'w').write(output_path)


if __name__ == '__main__':
    main()
