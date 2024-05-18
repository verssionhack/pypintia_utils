from dataclasses import dataclass
from typing import *

@dataclass
class ExampleTestDatasItem:
    name: str
    input: str
    output: str




    def __init__(self, data: dict):

        self.name = data.get('name')
        self.input = data.get('input')
        self.output = data.get('output')



@dataclass
class ProgrammingProblemConfig:
    time_limit: int
    memory_limit: int
    code_size_limit: int
    cases: dict
    example_test_datas: List[ExampleTestDatasItem]
    testdata_description_code: str
    customize_limits: list
    stack_size_limit: int
    tools: list
    ignore_presentation_error: bool
    path_as_stdin: str
    path_as_stdout: str




    def __init__(self, data: dict):

        self.time_limit = data.get('time_limit')
        self.memory_limit = data.get('memory_limit')
        self.code_size_limit = data.get('code_size_limit')
        self.cases = data.get('cases')
        self.example_test_datas = [ExampleTestDatasItem(i) for i in (data.get('example_test_datas') if data.get('example_test_datas') != None else [])]
        self.testdata_description_code = data.get('testdata_description_code')
        self.customize_limits = data.get('customize_limits')
        self.stack_size_limit = data.get('stack_size_limit')
        self.tools = data.get('tools')
        self.ignore_presentation_error = data.get('ignore_presentation_error')
        self.path_as_stdin = data.get('path_as_stdin')
        self.path_as_stdout = data.get('path_as_stdout')



@dataclass
class ProblemConfig:
    programming_problem_config: ProgrammingProblemConfig
    solution_visible: bool
    answer_visible: bool




    def __init__(self, data: dict):

        self.programming_problem_config = ProgrammingProblemConfig(data.get('programming_problem_config'))
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
class ProblemExamProblem:
    problem_set_problem: ProblemSetProblem
    organization: Organization




    def __init__(self, data: dict):

        self.problem_set_problem = ProblemSetProblem(data.get('problem_set_problem'))
        self.organization = Organization(data.get('organization'))



