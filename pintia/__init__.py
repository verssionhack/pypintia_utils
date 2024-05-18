from .problem_exam import ProblemExam
from .problem_ranking import ProblemRanking
from .problem_exam_list import ProblemExamList
from .problem_status import ProblemStatus
from .problem_types import ProblemTypes
from .problem_exam_problem import ProblemExamProblem
from .problem_sets import ProblemSets

from .profile import Profile
from .user import UserPacket as User
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
