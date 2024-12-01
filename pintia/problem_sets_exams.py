from dataclasses import dataclass
from typing import List, Dict


@dataclass
class ExamConfig:

    def __init__(self, data: dict | None):
        if data is None:
            return None





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
class Exam:
    id: str
    score: float
    start_at: str
    end_at: str
    accept_count: int
    exam_config: ExamConfig
    student_user: StudentUser
    problem_set_id: str
    user_id: str
    ended: bool
    status: str
    reset_status: bool
    adjust_amount: int
    adjusted_score: int

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.id = data.get("id")
        self.score = data.get("score")
        self.start_at = data.get("start_at")
        self.end_at = data.get("end_at")
        self.accept_count = data.get("accept_count")
        self.exam_config = ExamConfig(data.get("exam_config"))
        self.student_user = StudentUser(data.get("student_user"))
        self.problem_set_id = data.get("problem_set_id")
        self.user_id = data.get("user_id")
        self.ended = data.get("ended")
        self.status = data.get("status")
        self.reset_status = data.get("reset_status")
        self.adjust_amount = data.get("adjust_amount")
        self.adjusted_score = data.get("adjusted_score")





@dataclass
class ProblemSetConfig:
    compilers: List[str]
    multiple_choice_more_than_one_answer_problem_scoring_method: str
    scoring_rule: str
    hide_scoreboard: bool
    hiding_time: int
    show_name_in_ranking: bool
    hide_other_problem_sets: bool
    allow_student_login: bool
    allowed_login_seconds_before_start: int
    oms_protected: bool
    allow_submit_exam: bool
    problem_type_order: list
    use_strict_code_judger: bool
    show_bulletin_board: bool
    show_detections: bool
    exam_group_id: str
    enable_custom_test_data: bool
    enable_virtual_printer: bool
    blind_judge_subjective: bool
    auto_save: bool
    forbid_pasting: bool
    allow_add_collection: bool
    allow_filter_user_group: bool
    has_grading: bool
    enable_xcpc_contest_service: bool
    collection_derived_problem_set_id: str
    show_difficulty: bool
    post_pay_account_id: str
    post_pay_account_type: str
    hide_programming_judge_response_contents: bool
    hide_score: bool
    enable_ai: bool
    enable_competition_service: bool

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.compilers = [str(i) for i in (data.get("compilers") if data.get("compilers") is not None else [])]
        self.multiple_choice_more_than_one_answer_problem_scoring_method = data.get("multiple_choice_more_than_one_answer_problem_scoring_method")
        self.scoring_rule = data.get("scoring_rule")
        self.hide_scoreboard = data.get("hide_scoreboard")
        self.hiding_time = data.get("hiding_time")
        self.show_name_in_ranking = data.get("show_name_in_ranking")
        self.hide_other_problem_sets = data.get("hide_other_problem_sets")
        self.allow_student_login = data.get("allow_student_login")
        self.allowed_login_seconds_before_start = data.get("allowed_login_seconds_before_start")
        self.oms_protected = data.get("oms_protected")
        self.allow_submit_exam = data.get("allow_submit_exam")
        self.problem_type_order = data.get("problem_type_order")
        self.use_strict_code_judger = data.get("use_strict_code_judger")
        self.show_bulletin_board = data.get("show_bulletin_board")
        self.show_detections = data.get("show_detections")
        self.exam_group_id = data.get("exam_group_id")
        self.enable_custom_test_data = data.get("enable_custom_test_data")
        self.enable_virtual_printer = data.get("enable_virtual_printer")
        self.blind_judge_subjective = data.get("blind_judge_subjective")
        self.auto_save = data.get("auto_save")
        self.forbid_pasting = data.get("forbid_pasting")
        self.allow_add_collection = data.get("allow_add_collection")
        self.allow_filter_user_group = data.get("allow_filter_user_group")
        self.has_grading = data.get("has_grading")
        self.enable_xcpc_contest_service = data.get("enable_xcpc_contest_service")
        self.collection_derived_problem_set_id = data.get("collection_derived_problem_set_id")
        self.show_difficulty = data.get("show_difficulty")
        self.post_pay_account_id = data.get("post_pay_account_id")
        self.post_pay_account_type = data.get("post_pay_account_type")
        self.hide_programming_judge_response_contents = data.get("hide_programming_judge_response_contents")
        self.hide_score = data.get("hide_score")
        self.enable_ai = data.get("enable_ai")
        self.enable_competition_service = data.get("enable_competition_service")





@dataclass
class Connections:

    def __init__(self, data: dict | None):
        if data is None:
            return None





@dataclass
class ProblemSet:
    id: str
    name: str
    description: str
    type: str
    time_type: str
    problem_set_config: ProblemSetConfig
    start_at: str
    end_at: str
    duration: int
    share_code: str
    manageable: bool
    collaborator_permission: str
    owner_organization_id: str
    owner_id: str
    hide: bool
    stage: str
    announcement: str
    internal: bool
    feature: str
    batch_judge_at: str
    connections: Connections

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.id = data.get("id")
        self.name = data.get("name")
        self.description = data.get("description")
        self.type = data.get("type")
        self.time_type = data.get("time_type")
        self.problem_set_config = ProblemSetConfig(data.get("problem_set_config"))
        self.start_at = data.get("start_at")
        self.end_at = data.get("end_at")
        self.duration = data.get("duration")
        self.share_code = data.get("share_code")
        self.manageable = data.get("manageable")
        self.collaborator_permission = data.get("collaborator_permission")
        self.owner_organization_id = data.get("owner_organization_id")
        self.owner_id = data.get("owner_id")
        self.hide = data.get("hide")
        self.stage = data.get("stage")
        self.announcement = data.get("announcement")
        self.internal = data.get("internal")
        self.feature = data.get("feature")
        self.batch_judge_at = data.get("batch_judge_at")
        self.connections = Connections(data.get("connections"))





@dataclass
class Permission:
    permission: int

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.permission = data.get("permission")





@dataclass
class ProblemSetsExams:
    server_time: str
    exam: Exam
    problem_set: ProblemSet
    status: str
    permission: Permission
    collaborator_permission: str

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.server_time = data.get("server_time")
        self.exam = Exam(data.get("exam"))
        self.problem_set = ProblemSet(data.get("problem_set"))
        self.status = data.get("status")
        self.permission = Permission(data.get("permission"))
        self.collaborator_permission = data.get("collaborator_permission")




