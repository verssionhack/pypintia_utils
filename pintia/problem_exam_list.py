from dataclasses import dataclass
from typing import *
@dataclass
class ProblemSetProblemsItem:
    id: str
    label: str
    score: int
    deadline: str
    accept_count: int
    submit_count: int
    title: str
    type: str
    difficulty: int
    compiler: str
    problem_status: str
    problem_set_id: str
    problem_pool_index: int
    index_in_problem_pool: int




    def __init__(self, data: dict):

        self.id = data.get('id')
        self.label = data.get('label')
        self.score = data.get('score')
        self.deadline = data.get('deadline')
        self.accept_count = data.get('accept_count')
        self.submit_count = data.get('submit_count')
        self.title = data.get('title')
        self.type = data.get('type')
        self.difficulty = data.get('difficulty')
        self.compiler = data.get('compiler')
        self.problem_status = data.get('problem_status')
        self.problem_set_id = data.get('problem_set_id')
        self.problem_pool_index = data.get('problem_pool_index')
        self.index_in_problem_pool = data.get('index_in_problem_pool')



@dataclass
class ProblemExamList:
    total: int
    problem_set_problems: List[ProblemSetProblemsItem]




    def __init__(self, data: dict):

        self.total = data.get('total')
        self.problem_set_problems = [ProblemSetProblemsItem(i) for i in (data.get('problem_set_problems') if data.get('problem_set_problems') != None else [])]



