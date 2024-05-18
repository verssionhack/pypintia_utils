from dataclasses import dataclass
from typing import List

@dataclass
class Case:
    hint: str
    show_hint: bool
    score: int
    is_public: bool




    def __init__(self, data: dict):

        self.hint = data.get('hint')
        self.show_hint = data.get('show_hint')
        self.score = data.get('score')
        self.is_public = data.get('is_public')



@dataclass
class CodeCompletionProblemConfig:
    time_limit: int
    memory_limit: int
    code_size_limit: int
    cases: List[Case]
    example_test_datas: list
    testdata_description_code: str
    tools: list
    ignore_presentation_error: bool
    path_as_stdin: str
    path_as_stdout: str




    def __init__(self, data: dict):

        self.time_limit = data.get('time_limit')
        self.memory_limit = data.get('memory_limit')
        self.code_size_limit = data.get('code_size_limit')
        self.cases = [Case(i) for i in (data.get('cases').values() if data.get('cases') != None else [])]
        self.example_test_datas = data.get('example_test_datas')
        self.testdata_description_code = data.get('testdata_description_code')
        self.tools = data.get('tools')
        self.ignore_presentation_error = data.get('ignore_presentation_error')
        self.path_as_stdin = data.get('path_as_stdin')
        self.path_as_stdout = data.get('path_as_stdout')



@dataclass
class ProblemConfig:
    code_completion_problem_config: CodeCompletionProblemConfig
    solution_visible: bool
    answer_visible: bool




    def __init__(self, data: dict):

        self.code_completion_problem_config = CodeCompletionProblemConfig(data.get('code_completion_problem_config'))
        self.solution_visible = data.get('solution_visible')
        self.answer_visible = data.get('answer_visible')



@dataclass
class ProblemSetProblem:
    id: str
    label: str
    score: int
    problem_config: ProblemConfig
    deadline: str
    title: str
    content: str
    type: str
    author: str
    difficulty: int
    compiler: str
    problem_status: str
    last_submission_id: str
    solution: str
    problem_set_id: str
    problem_id: str
    description: str
    problem_pool_index: int
    index_in_problem_pool: int
    author_organization_id: str




    def __init__(self, data: dict):

        self.id = data.get('id')
        self.label = data.get('label')
        self.score = data.get('score')
        self.problem_config = ProblemConfig(data.get('problem_config'))
        self.deadline = data.get('deadline')
        self.title = data.get('title')
        self.content = data.get('content')
        self.type = data.get('type')
        self.author = data.get('author')
        self.difficulty = data.get('difficulty')
        self.compiler = data.get('compiler')
        self.problem_status = data.get('problem_status')
        self.last_submission_id = data.get('last_submission_id')
        self.solution = data.get('solution')
        self.problem_set_id = data.get('problem_set_id')
        self.problem_id = data.get('problem_id')
        self.description = data.get('description')
        self.problem_pool_index = data.get('problem_pool_index')
        self.index_in_problem_pool = data.get('index_in_problem_pool')
        self.author_organization_id = data.get('author_organization_id')



@dataclass
class Organization:
    id: str
    name: str
    code: str
    type: str
    logo: str




    def __init__(self, data: dict):

        self.id = data.get('id')
        self.name = data.get('name')
        self.code = data.get('code')
        self.type = data.get('type')
        self.logo = data.get('logo')



@dataclass
class ExamProblem:
    problem_set_problem: ProblemSetProblem
    organization: Organization




    def __init__(self, data: dict):

        self.problem_set_problem = ProblemSetProblem(data.get('problem_set_problem'))
        self.organization = Organization(data.get('organization'))



