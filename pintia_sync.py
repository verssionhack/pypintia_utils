#!/bin/python3


import sys
import os
import os.path as op
from time import sleep
from pintia import Pintia, ProblemSubmissionStatus, ProblemType
import json as j
from pintia.problem_sets import ProblemSetsItem
from pintia.problem_status import ProblemStatus
from utils import load_cookie, parse_select_args, random_chars, format_c_code

class Syncer:
    loaded_cookies = set()
    api_pool = {}
    cookies_path = None
    selecteds = []
    problem_sets = []
    exams_problems = {}

    def reload_apis(self):
        cookies = set([open(op.join(self.cookies_path, i), 'r').read() for i in os.listdir(self.cookies_path)])
        for cookie in cookies:
            if cookie in self.loaded_cookies:
                continue
            try:
                api = Pintia(cookie)
                self.api_pool[api._profile.user.id] = {
                        'api': api,
                        }
                self.loaded_cookies.add(cookie)
            except:
                pass

    def __init__(self, cookies_path):
        self.cookies_path = cookies_path


    def select_problem_sets(self):
        has_problem_ids = [i['problem_sets_id'] for i in self.problem_sets]
        for user_id, handle in self.api_pool.items():
            api = handle['api']
            handle['problem_sets'] = {}
            for problem_set in api.problem_sets(20).problem_sets:
                if problem_set.id not in handle['problem_sets']:

                    handle['problem_sets'][problem_set.id] = {}
                if problem_set.id not in has_problem_ids:

                    self.exams_problems[problem_set.id] = {}

                    has_problem_ids.append(problem_set.id)
                    self.problem_sets.append({
                            'problem_sets_id': problem_set.id,
                            'status': problem_set.status,
                            'name': problem_set.name,
                            'owner_name': problem_set.owner_nickname,
                            'start_at': problem_set.start_at,
                            'end_at': problem_set.end_at,
                            'duration': problem_set.duration,
                            })
        for i in range(len(self.problem_sets)):
            p = self.problem_sets[i]
            print(f'[{i}] name={p["name"]} id={p["problem_sets_id"]} status={p["status"]}')
        self.selecteds = parse_select_args(input(f'Select 0-{len(self.problem_sets) - 1}? '))

    def fetch_accpeted_problems(self):
        for user_id, handle in self.api_pool.items():
            api = handle['api']

            for selected in self.selecteds:
                problem_set = self.problem_sets[selected]
                problem_set_id = problem_set['problem_sets_id']


                if problem_set['status'] not in ['PROCESSING', 'PENDING']:
                    api.problem_sets_exams_start(problem_set_id)

                #if problem_set_id in handle['problem_sets'] and handle['problem_sets'][problem_set_id].get('status') == None:
                #print(api.problem_sets_exams_start(problem_set_id))

                handle['problem_sets'][problem_set_id]['status'] = api.problem_sets_status(problem_set_id)
                problem_set_status = handle['problem_sets'][problem_set_id]['status']
                for problem in problem_set:
                    if problem.id not in self.exams_problems[problem_set_id] and problem.problem_submission_status == ProblemSubmissionStatus.PROBLEM_ACCEPTED.value:

                        print(f'{api._profile.user.nickname} provide {problem_set["name"]}:{problem.id}')
                        last_submission = api.problem_sets_exam_problem_last_submissions(problem_set_id, problem.id)
                        if problem.problem_type == ProblemType.CODE_COMPLETION.value:
                            self.exams_problems[problem_set_id][problem.id] = {
                                    'problem_set_problem_id': problem.id,
                                    'compiler': last_submission.submission.compiler,
                                    'program_content': format_c_code(last_submission.submission.submission_details[-1].code_completion_submission_detail.program),
                                    'problem_type': last_submission.submission.problem_type,
                                    }
                        if problem.problem_type == ProblemType.PROGRAMMING.value:
                            self.exams_problems[problem_set_id][problem.id] = {
                                    'problem_set_problem_id': problem.id,
                                    'compiler': last_submission.submission.compiler,
                                    'program_content': format_c_code(last_submission.submission.submission_details[-1].programming_submission_detail.program),
                                    'problem_type': last_submission.submission.problem_type,
                                    }

    def sync(self):
        for user_id, handle in self.api_pool.items():
            api = handle['api']

            for selected in self.selecteds:
                problem_set = self.problem_sets[selected]
                problem_set_id = problem_set['problem_sets_id']

                exams = api.problem_sets_exams(problem_set_id)

                if problem_set_id in handle['problem_sets']:
                    problem_set_status = handle['problem_sets'][problem_set_id]['status']

                    for problem in problem_set_status.problem_status:
                        if problem.id in self.exams_problems[problem_set_id] and problem.problem_submission_status != ProblemSubmissionStatus.PROBLEM_ACCEPTED.value:
                            api.problem_sets_exam_problem_submission(**self.exams_problems[problem_set_id][problem.id], exam_id=exams.exam.id)
                            print(f'Sync submission {problem_set["name"]}:{problem.id} for {api._profile.user.nickname}')




def main():
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} <cookie_pool_path>')
        exit(-1)

    syncer = Syncer(sys.argv[1])
    syncer.reload_apis()
    syncer.select_problem_sets()

    while True:
        try:
            syncer.reload_apis()
            syncer.fetch_accpeted_problems()
            syncer.sync()
        except KeyboardInterrupt:
            print('Exit')
            exit()
        except Exception as e:
            print(f'Error: {e}')
        #print(f'{k}: count={len(v)}', end='\n', flush=True)
        sleep(1)



if __name__ == '__main__':
    main()
