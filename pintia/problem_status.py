from dataclasses import dataclass
from typing import *
@dataclass
class ProblemStatusItem:
    id: str
    label: str
    score: int
    problem_submission_status: str
    problem_type: str
    problem_pool_index: int
    index_in_problem_pool: int




    def __init__(self, data: dict):

        self.id = data.get('id')
        self.label = data.get('label')
        self.score = data.get('score')
        self.problem_submission_status = data.get('problem_submission_status')
        self.problem_type = data.get('problem_type')
        self.problem_pool_index = data.get('problem_pool_index')
        self.index_in_problem_pool = data.get('index_in_problem_pool')



@dataclass
class ProblemStatus:
    problem_status: List[ProblemStatusItem]




    def __init__(self, data: dict):

        self.problem_status = [ProblemStatusItem(i) for i in (data.get('problem_status') if data.get('problem_status') != None else [])]



