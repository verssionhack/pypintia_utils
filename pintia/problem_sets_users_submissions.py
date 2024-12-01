from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Submissions:
    id: str
    user_id: str
    problem_type: str
    problem_set_problem_id: str
    submit_at: str
    status: str
    score: float
    compiler: str
    time: float
    memory: int
    preview_submission: bool
    judge_at: str

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.id = data.get("id")
        self.user_id = data.get("user_id")
        self.problem_type = data.get("problem_type")
        self.problem_set_problem_id = data.get("problem_set_problem_id")
        self.submit_at = data.get("submit_at")
        self.status = data.get("status")
        self.score = data.get("score")
        self.compiler = data.get("compiler")
        self.time = data.get("time")
        self.memory = data.get("memory")
        self.preview_submission = data.get("preview_submission")
        self.judge_at = data.get("judge_at")





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
class ExamMember:
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
class ProblemSetsUsersSubmissions:
    submissions: List[Submissions]
    has_after: bool
    has_before: bool
    problem_set_problem_by_id: dict
    exam_member: ExamMember
    show_detail_by_submission_id: dict
    exam_label_by_problem_set_problem_id: dict

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.submissions = [Submissions(i) for i in (data.get("submissions") if data.get("submissions") is not None else [])]
        self.has_after = data.get("has_after")
        self.has_before = data.get("has_before")
        self.problem_set_problem_by_id = data.get("problem_set_problem_by_id")
        self.exam_member = ExamMember(data.get("exam_member"))
        self.show_detail_by_submission_id = data.get("show_detail_by_submission_id")
        self.exam_label_by_problem_set_problem_id = data.get("exam_label_by_problem_set_problem_id")




