HOST = 'pintia.cn'


import requests as r
from .user_current import UserCurrent
from .users_profile import UsersProfile
from .problem_sets_exams import ProblemSetsExams
from .problem_sets_exam_problem_status import ProblemSetsExamProblemStatus
from .problem_sets_exam_problems import ProblemSetsExamProblems
from .problem_sets_exam_problem_list import ProblemSetsExamProblemList
from .problem_exam import ProblemExam
from .problem_exam_problem import ProblemExamProblem
from .last_submissions import LastSubmissions
from .problem_ranking import ProblemRanking
from .problem_types import ProblemTypes
from .problem_sets import ProblemSets
from .utils import dict_key2snake_name, parse_cookie
import time

DATE = time.gmtime()

import json as j


USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'

class Pintia:

    def load_cookie(self, cookie: dict | str):
        if type(cookie) == type(''):
            cookie = parse_cookie(cookie)
        self.cookie = cookie
        self.session.cookies.update(self.cookie)
        self._profile = self.current_user()
        print(f'Load as {self._profile.user.nickname}')


    def __init__(self, cookie: dict | str | None = None):
        self.url = f'https://pintia.cn'
        self.session = r.session()
        self.session.headers['user-agent'] = USER_AGENT
        self.session.headers['accept'] = 'application/json;charset=UTF-8'
        self.last_request_time = time.time()


        self._profile = None
        if cookie != None:
            self.load_cookie(cookie)

    def update_last_request_time(self):
        now = time.time()
        if now - self.last_request_time < 0.2:
            time.sleep(0.2)
        self.last_request_time = now


    def on_rate_limit(self, content):
        if 'RATE_LIMIT_EXCEEDED' in content:
            rate_rest = 3
            while rate_rest > 0:
                print(f'Sleep {rate_rest}s: {content}', end='\r', flush=True)
                time.sleep(1)
                rate_rest -= 1
            return True
        return False


    def _get(self, uri: str, **args):
        self.update_last_request_time()
        ret = self.session.get(self.url + uri, **args)
        if ret.status_code != 200:
            if self.on_rate_limit(ret.text):
                return self._get(uri, **args)
            print(f'status={ret.status_code} uri={uri}')
            print(f'response={ret.text}')
            input()
        try:
            ret_json = ret.json()
            dict_key2snake_name(ret_json)
            #print(j.dumps(ret_json, ensure_ascii=0, indent=4))
            return ret_json
        except Exception as e:
            print(f'error for {uri}: {e}')
            print(f'reply={ret.text}')
            input()


    def _post(self, uri: str, **args):
        self.update_last_request_time()
        ret = self.session.post(self.url + uri, **args)
        if ret.status_code != 200:
            if self.on_rate_limit(ret.text):
                return self._post(uri, **args)
            print(f'status={ret.status_code} uri={uri}')
            print(f'response={ret.text}')
            input()
        try:
            ret_json = ret.json()
            dict_key2snake_name(ret_json)
            #print(j.dumps(ret_json, ensure_ascii=0, indent=4))
            return ret_json
        except Exception as e:
            print(f'error for {uri}: {e}')
            print(f'reply={ret.text}')
            input()

    def profile(self):
        uri = '/api/users/profile'
        return Profile(self._get(uri))

    def current_user(self):
        uri = '/api/u/current'
        return UserPacket(self._get(uri))

    #def problem_sets(self, limit: int, filter=f'{{"endAtAfter": "{DATE.tm_year:04}-{DATE.tm_mon:02}-{DATE.tm_mday-1:02}T16:00:00.000Z"}}', order_by='END_AT', asc=True):
    def problem_sets(self, limit: int, filter=f'{{"endAtAfter": "{DATE.tm_year:04}-{DATE.tm_mon:02}-{DATE.tm_mday:02}T{DATE.tm_hour:02}:{DATE.tm_min:02}:00.000Z"}}', order_by='END_AT', asc=True):
        uri = f'/api/problem-sets?filter={filter}&limit={limit}&order_by={order_by}&asc={str(asc).lower()}'
        return ProblemSets(self._get(uri))

    def problem_sets_exams(self, problem_sets_id: str):
        uri = f'/api/problem-sets/{problem_sets_id}/exams'
        return Exams(self._get(uri))

    def problem_sets_exams_start(self, problem_sets_id: str):
        uri = f'/api/problem-sets/{problem_sets_id}/exams'
        return self._post(uri)

    def problem_sets_summaries(self, problem_sets_id: str):
        uri = f'/api/problem-sets/{problem_sets_id}/problem-summaries'
        pass

    def problem_sets_status(self, problem_sets_id: str):
        uri = f'/api/problem-sets/{problem_sets_id}/exam-problem-status'
        return ProblemStatus(self._get(uri))

    def problem_sets_exam_list(self, problem_sets_id: str, exam_id: str, problem_type, page: int, limit: int):
        uri = f'/api/problem-sets/{problem_sets_id}/exam-problem-list?exam_id={exam_id}&problem_type={problem_type}&page={page}&limit={limit}'
        return ProblemExamList(self._get(uri))

    def problem_sets_exam(self, problem_sets_id: str, exam_problem_id: str, problem_type):
        uri = f'/api/problem-sets/{problem_sets_id}/exam-problems/?exam_id={exam_problem_id}&problem_type={problem_type}'
        return ProblemExam(self._get(uri))

    def problem_sets_exam_problem(self, problem_sets_id: str, exam_problem_id: str):
        uri = f'/api/problem-sets/{problem_sets_id}/exam-problems/{exam_problem_id}'
        return ProblemExamProblem(self._get(uri))

    def problem_sets_exam_problem_submission(self, exam_id: str, problem_set_problem_id: str, compiler: str, program_content: str, problem_type: str):
        uri = f'/api/exams/{exam_id}/submissions'
        return self._post(uri, json= {
            'details':[{
                'problemId': '0',
                'problemSetProblemId': problem_set_problem_id,
                'programmingSubmissionDetail': {
                    'program': program_content,
                    'compiler': compiler.upper(),
                    }
                }],
            'problemType': problem_type,
            })

    def problem_sets_exam_problem_last_submissions(self, problem_sets_id: str, exam_problem_id: str):
        uri = f'/api/problem-sets/{problem_sets_id}/last-submissions?problem_set_problem_id={exam_problem_id}'
        return LastSubmissions(self._get(uri))



    def problem_sets_rankings(self, problem_sets_id: str, page: int, limit: int):
        uri = f'/api/problem-sets/{problem_sets_id}/rankings?page={page}&limit={limit}'
        return ProblemRanking(self._get(uri))

    def problem_types(self, problem_sets_id: str):
        uri = f'/api/problem-sets/{problem_sets_id}/problem-types'
        return ProblemTypes(self._get(uri))

    def login(self, phone: str, password: str):
        uri = '/api/users/sessions'
        payload = {
                'phone': phone,
                'password': password,
                'rememberMe': False,
                }

        ret = self.session.post('https://passport.pintia.cn' + uri, json=payload)

        if ret.status_code != 200:
            print(f'status={ret.status_code} uri={uri}')
            print(f'response={ret.text}')
            input()

        self._profile = self.current_user()
        print(f'Load as {self._profile.user.nickname}')
    

