from dataclasses import dataclass
from typing import *
@dataclass
class LabelsItem:
    id: str
    label: str
    title: str
    type: str
    problem_pool_index: int
    index_in_problem_pool: int




    def __init__(self, data: dict):

        self.id = data.get('id')
        self.label = data.get('label')
        self.title = data.get('title')
        self.type = data.get('type')
        self.problem_pool_index = data.get('problem_pool_index')
        self.index_in_problem_pool = data.get('index_in_problem_pool')



@dataclass
class ProblemTypes:
    labels: List[LabelsItem]
    problem_types: List[str]




    def __init__(self, data: dict):

        self.labels = [LabelsItem(i) for i in (data.get('labels') if data.get('labels') != None else [])]
        self.problem_types = data.get('problem_types')



