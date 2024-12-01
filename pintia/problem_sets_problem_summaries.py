from dataclasses import dataclass
from typing import List, Dict


@dataclass
class TrueOrFalse:
    total: int
    total_score: int

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.total = data.get("total")
        self.total_score = data.get("total_score")





@dataclass
class MultipleChoice:
    total: int
    total_score: int

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.total = data.get("total")
        self.total_score = data.get("total_score")





@dataclass
class CodeCompletion:
    total: int
    total_score: int

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.total = data.get("total")
        self.total_score = data.get("total_score")





@dataclass
class Programming:
    total: int
    total_score: int

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.total = data.get("total")
        self.total_score = data.get("total_score")





@dataclass
class Summaries:
    true_or_false: TrueOrFalse
    multiple_choice: MultipleChoice
    code_completion: CodeCompletion
    programming: Programming

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.true_or_false = TrueOrFalse(data.get("true_or_false"))
        self.multiple_choice = MultipleChoice(data.get("multiple_choice"))
        self.code_completion = CodeCompletion(data.get("code_completion"))
        self.programming = Programming(data.get("programming"))





@dataclass
class ProblemSetsProblemSummaries:
    summaries: Summaries

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.summaries = Summaries(data.get("summaries"))




