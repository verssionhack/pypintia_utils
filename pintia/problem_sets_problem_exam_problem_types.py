from dataclasses import dataclass
from typing import *

@dataclass
class Labels:
    id: str
    label: str
    score: int
    problem_pool_index: int
    problem_pool_composition_count: int
    title: str
    type: str
    index_in_problem_pool: int

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.id = data.get("id")
        self.label = data.get("label")
        self.score = data.get("score")
        self.problem_pool_index = data.get("problem_pool_index")
        self.problem_pool_composition_count = data.get("problem_pool_composition_count")
        self.title = data.get("title")
        self.type = data.get("type")
        self.index_in_problem_pool = data.get("index_in_problem_pool")





@dataclass
class ProblemSetsProblemExamProblemTypes:
    labels: List[Labels]
    problem_types: List[str]
    exam_label_by_problem_set_problem_id: dict

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.labels = [Labels(i) for i in (data.get("labels") if data.get("labels") != None else [])]
        self.problem_types = [str(i) for i in (data.get("problem_types") if data.get("problem_types") != None else [])]
        self.exam_label_by_problem_set_problem_id = data.get("exam_label_by_problem_set_problem_id")




