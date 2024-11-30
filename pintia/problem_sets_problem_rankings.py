from dataclasses import dataclass
from typing import *

@dataclass
class User:
    id: str
    nickname: str

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.id = data.get("id")
        self.nickname = data.get("nickname")





@dataclass
class StudentUser:
    student_number: str
    name: str
    id: str

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.student_number = data.get("student_number")
        self.name = data.get("name")
        self.id = data.get("id")





@dataclass
class User:
    user: User
    student_user: StudentUser
    user_group_id: str
    exam_id: str

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.user = User(data.get("user"))
        self.student_user = StudentUser(data.get("student_user"))
        self.user_group_id = data.get("user_group_id")
        self.exam_id = data.get("exam_id")





@dataclass
class TypeScores:
    code_completion: float

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.code_completion = data.get("code_completion")





@dataclass
class CommonRankings:
    rank: int
    user: User
    exam_id: str
    total_score: float
    type_scores: TypeScores
    solving_time: int
    problem_score_by_problem_set_problem_id: dict
    start_at: str

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.rank = data.get("rank")
        self.user = User(data.get("user"))
        self.exam_id = data.get("exam_id")
        self.total_score = data.get("total_score")
        self.type_scores = TypeScores(data.get("type_scores"))
        self.solving_time = data.get("solving_time")
        self.problem_score_by_problem_set_problem_id = data.get("problem_score_by_problem_set_problem_id")
        self.start_at = data.get("start_at")





@dataclass
class TypeScores:
    code_completion: float
    programming: float

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.code_completion = data.get("code_completion")
        self.programming = data.get("programming")





@dataclass
class SelfRanking:
    rank: int
    user: User
    exam_id: str
    total_score: float
    type_scores: TypeScores
    solving_time: int
    problem_score_by_problem_set_problem_id: dict
    start_at: str

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.rank = data.get("rank")
        self.user = User(data.get("user"))
        self.exam_id = data.get("exam_id")
        self.total_score = data.get("total_score")
        self.type_scores = TypeScores(data.get("type_scores"))
        self.solving_time = data.get("solving_time")
        self.problem_score_by_problem_set_problem_id = data.get("problem_score_by_problem_set_problem_id")
        self.start_at = data.get("start_at")





@dataclass
class CommonRankings:
    labels: List[str]
    common_rankings: List[CommonRankings]
    self_ranking: SelfRanking
    label_by_problem_set_problem_id: dict

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.labels = [str(i) for i in (data.get("labels") if data.get("labels") != None else [])]
        self.common_rankings = [CommonRankings(i) for i in (data.get("common_rankings") if data.get("common_rankings") != None else [])]
        self.self_ranking = SelfRanking(data.get("self_ranking"))
        self.label_by_problem_set_problem_id = data.get("label_by_problem_set_problem_id")





@dataclass
class ProblemSetsProblemRankings:
    total: int
    common_rankings: CommonRankings

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.total = data.get("total")
        self.common_rankings = CommonRankings(data.get("common_rankings"))




