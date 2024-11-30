from dataclasses import dataclass
from typing import *

@dataclass
class ProblemSets:
    id: str
    name: str
    type: str
    time_type: str
    status: str
    organization_name: str
    owner_nickname: str
    manageable: bool
    create_at: str
    update_at: str
    scoring_rule: str
    organization_type: str
    owner_id: str
    start_at: str
    end_at: str
    duration: int
    owner_organization_id: str
    stage: str
    feature: str
    source_problem_set_id: str

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.id = data.get("id")
        self.name = data.get("name")
        self.type = data.get("type")
        self.time_type = data.get("time_type")
        self.status = data.get("status")
        self.organization_name = data.get("organization_name")
        self.owner_nickname = data.get("owner_nickname")
        self.manageable = data.get("manageable")
        self.create_at = data.get("create_at")
        self.update_at = data.get("update_at")
        self.scoring_rule = data.get("scoring_rule")
        self.organization_type = data.get("organization_type")
        self.owner_id = data.get("owner_id")
        self.start_at = data.get("start_at")
        self.end_at = data.get("end_at")
        self.duration = data.get("duration")
        self.owner_organization_id = data.get("owner_organization_id")
        self.stage = data.get("stage")
        self.feature = data.get("feature")
        self.source_problem_set_id = data.get("source_problem_set_id")





@dataclass
class HomeworkByProblemSetId:

    def __init__(self, data: dict | None):
        if data is None:
            return None





@dataclass
class ProblemSets:
    total: int
    problem_sets: List[ProblemSets]
    homework_by_problem_set_id: HomeworkByProblemSetId

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.total = data.get("total")
        self.problem_sets = [ProblemSets(i) for i in (data.get("problem_sets") if data.get("problem_sets") != None else [])]
        self.homework_by_problem_set_id = HomeworkByProblemSetId(data.get("homework_by_problem_set_id"))




