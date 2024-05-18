from dataclasses import dataclass
from typing import *
@dataclass
class MultipleChoiceProblemConfig:
    choices: List[str]
    max_display_choices_per_line: int




    def __init__(self, data: dict):

        self.choices = data.get('choices')
        self.max_display_choices_per_line = data.get('max_display_choices_per_line')



@dataclass
class ProblemConfig:
    solution_visible: bool
    answer_visible: bool
    multiple_choice_problem_config: MultipleChoiceProblemConfig




    def __init__(self, data: dict):

        self.solution_visible = data.get('solution_visible')
        self.answer_visible = data.get('answer_visible')
        self.multiple_choice_problem_config = MultipleChoiceProblemConfig(data.get('multiple_choice_problem_config'))



@dataclass
class ProblemSetProblemsItem:
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
class ProblemExam:
    organization_by_id: dict
    problem_set_problems: List[ProblemSetProblemsItem]




    def __init__(self, data: dict):

        self.organization_by_id = data.get('organization_by_id')
        self.problem_set_problems = [ProblemSetProblemsItem(i) for i in (data.get('problem_set_problems') if data.get('problem_set_problems') != None else [])]



