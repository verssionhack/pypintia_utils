from dataclasses import dataclass
from typing import *
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




    def __init__(self, data: dict):

        self.compilers = data.get('compilers')
        self.multiple_choice_more_than_one_answer_problem_scoring_method = data.get('multiple_choice_more_than_one_answer_problem_scoring_method')
        self.scoring_rule = data.get('scoring_rule')
        self.hide_scoreboard = data.get('hide_scoreboard')
        self.hiding_time = data.get('hiding_time')
        self.show_name_in_ranking = data.get('show_name_in_ranking')
        self.hide_other_problem_sets = data.get('hide_other_problem_sets')
        self.allow_student_login = data.get('allow_student_login')
        self.allowed_login_seconds_before_start = data.get('allowed_login_seconds_before_start')
        self.oms_protected = data.get('oms_protected')
        self.allow_submit_exam = data.get('allow_submit_exam')
        self.problem_type_order = data.get('problem_type_order')
        self.use_strict_code_judger = data.get('use_strict_code_judger')
        self.show_bulletin_board = data.get('show_bulletin_board')
        self.show_detections = data.get('show_detections')
        self.exam_group_id = data.get('exam_group_id')
        self.enable_custom_test_data = data.get('enable_custom_test_data')
        self.enable_virtual_printer = data.get('enable_virtual_printer')
        self.blind_judge_subjective = data.get('blind_judge_subjective')
        self.auto_save = data.get('auto_save')
        self.forbid_pasting = data.get('forbid_pasting')
        self.allow_add_collection = data.get('allow_add_collection')
        self.allow_filter_user_group = data.get('allow_filter_user_group')
        self.has_grading = data.get('has_grading')
        self.enable_xcpc_contest_service = data.get('enable_xcpc_contest_service')
        self.collection_derived_problem_set_id = data.get('collection_derived_problem_set_id')
        self.show_difficulty = data.get('show_difficulty')
        self.post_pay_account_id = data.get('post_pay_account_id')
        self.post_pay_account_type = data.get('post_pay_account_type')



@dataclass
class ProblemSetsItem:
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
    problem_set_config: ProblemSetConfig
    owner_organization_id: str
    stage: str
    feature: str




    def __init__(self, data: dict):

        self.id = data.get('id')
        self.name = data.get('name')
        self.type = data.get('type')
        self.time_type = data.get('time_type')
        self.status = data.get('status')
        self.organization_name = data.get('organization_name')
        self.owner_nickname = data.get('owner_nickname')
        self.manageable = data.get('manageable')
        self.create_at = data.get('create_at')
        self.update_at = data.get('update_at')
        self.scoring_rule = data.get('scoring_rule')
        self.organization_type = data.get('organization_type')
        self.owner_id = data.get('owner_id')
        self.start_at = data.get('start_at')
        self.end_at = data.get('end_at')
        self.duration = data.get('duration')
        self.problem_set_config = ProblemSetConfig(data.get('problem_set_config'))
        self.owner_organization_id = data.get('owner_organization_id')
        self.stage = data.get('stage')
        self.feature = data.get('feature')



@dataclass
class HomeworkByProblemSetId:




    def __init__(self, data: dict):

        pass



@dataclass
class ProblemSets:
    total: int
    problem_sets: List[ProblemSetsItem]
    homework_by_problem_set_id: HomeworkByProblemSetId




    def __init__(self, data: dict):

        self.total = data.get('total')
        self.problem_sets = [ProblemSetsItem(i) for i in (data.get('problem_sets') if data.get('problem_sets') != None else [])]
        self.homework_by_problem_set_id = HomeworkByProblemSetId(data.get('homework_by_problem_set_id'))



