from dataclasses import dataclass
from typing import *

@dataclass
class ProgrammingSubmissionDetail:
    compiler: str
    program: str

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.compiler = data.get("compiler")
        self.program = data.get("program")





@dataclass
class SubmissionDetails:
    problem_set_problem_id: str
    programming_submission_detail: ProgrammingSubmissionDetail
    problem_id: str

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.problem_set_problem_id = data.get("problem_set_problem_id")
        self.programming_submission_detail = ProgrammingSubmissionDetail(data.get("programming_submission_detail"))
        self.problem_id = data.get("problem_id")





@dataclass
class CompilationResult:
    log: str
    success: bool
    error: str

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.log = data.get("log")
        self.success = data.get("success")
        self.error = data.get("error")





@dataclass
class CheckerCompilationResult:
    log: str
    success: bool
    error: str

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.log = data.get("log")
        self.success = data.get("success")
        self.error = data.get("error")





@dataclass
class ProgrammingJudgeResponseContent:
    compilation_result: CompilationResult
    checker_compilation_result: CheckerCompilationResult
    testcase_judge_results: dict

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.compilation_result = CompilationResult(data.get("compilation_result"))
        self.checker_compilation_result = CheckerCompilationResult(data.get("checker_compilation_result"))
        self.testcase_judge_results = data.get("testcase_judge_results")





@dataclass
class JudgeResponseContents:
    status: str
    score: float
    programming_judge_response_content: ProgrammingJudgeResponseContent
    problem_set_problem_id: str

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.status = data.get("status")
        self.score = data.get("score")
        self.programming_judge_response_content = ProgrammingJudgeResponseContent(data.get("programming_judge_response_content"))
        self.problem_set_problem_id = data.get("problem_set_problem_id")





@dataclass
class Hints:

    def __init__(self, data: dict | None):
        if data is None:
            return None





@dataclass
class Submission:
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
    submission_details: List[SubmissionDetails]
    judge_response_contents: List[JudgeResponseContents]
    hints: Hints
    problem_set_id: str
    preview_submission: bool
    cause: str
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
        self.submission_details = [SubmissionDetails(i) for i in (data.get("submission_details") if data.get("submission_details") != None else [])]
        self.judge_response_contents = [JudgeResponseContents(i) for i in (data.get("judge_response_contents") if data.get("judge_response_contents") != None else [])]
        self.hints = Hints(data.get("hints"))
        self.problem_set_id = data.get("problem_set_id")
        self.preview_submission = data.get("preview_submission")
        self.cause = data.get("cause")
        self.judge_at = data.get("judge_at")





@dataclass
class ProblemSetsLastSubmissions:
    submission: Submission

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.submission = Submission(data.get("submission"))




