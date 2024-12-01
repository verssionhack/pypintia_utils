from .problem_sets_exam_problems import ProblemSetsExamProblems
from .problem_sets_problem_rankings import ProblemSetsProblemRankings
from .problem_sets_exam_problem_list import ProblemSetsExamProblemList
from .problem_sets_exam_problem_status import ProblemStatus
from .problem_sets_problem_exam_problem_types import ProblemSetsProblemExamProblemTypes
from .problem_sets_exam_problems import ProblemSetsExamProblems
from .problem_sets import ProblemSets

from .user_current import UserCurrent
from .exam_problem import ExamProblem
from .last_submissions import LastSubmissions
from .exams import Exams
from .utils import dict_key2snake_name, json2dataclass, pascal2snake, snake2pascal

from .api import Pintia

from enum import Enum


class ProblemType(Enum):
    PROGRAMMING = 'PROGRAMMING'
    CODE_COMPLETION = 'CODE_COMPLETION'
    MULTIPLE_CHOICE = 'MULTIPLE_CHOICE'
    MULTIPLE_CHOICE_MORE_THAN_ONE_ANSWER = 'MULTIPLE_CHOICE_MORE_THAN_ONE_ANSWER'


class ProblemSubmissionStatus(Enum):
    PROBLEM_NO_ANSWER = 'PROBLEM_NO_ANSWER'
    PROBLEM_ACCEPTED = 'PROBLEM_ACCEPTED'
    PROBLEM_WRONG_ANSWER = 'PROBLEM_WRONG_ANSWER'


class ExamStatus(Enum):
    PROCESSING = 'PROCESSING'
    END = 'END'


class ProblemSetsType(Enum):
    EXERCISE = 'EXERCISE'
