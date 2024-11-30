from dataclasses import dataclass
from typing import *

@dataclass
class ProblemStatus:
    id: str
    label: str
    score: int
    problem_submission_status: str
    problem_type: str
    problem_pool_index: int
    index_in_problem_pool: int

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.id = data.get("id")
        self.label = data.get("label")
        self.score = data.get("score")
        self.problem_submission_status = data.get("problem_submission_status")
        self.problem_type = data.get("problem_type")
        self.problem_pool_index = data.get("problem_pool_index")
        self.index_in_problem_pool = data.get("index_in_problem_pool")





@dataclass
class ProblemSetsExamProblemStatus:
    problem_status: List[ProblemStatus]
    exam_label_by_problem_set_problem_id: dict

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.problem_status = [ProblemStatus(i) for i in (data.get("problem_status") if data.get("problem_status") != None else [])]
        self.exam_label_by_problem_set_problem_id = data.get("exam_label_by_problem_set_problem_id")




