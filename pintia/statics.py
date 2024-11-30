from dataclasses import dataclass
from typing import *

@dataclass
class SiteStatistics:
    name: str
    teacher_count: int
    problem_count: int
    organization_count: int
    user_count: int
    course_count: int
    knowledge_point_count: int
    problem_set_count: int

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.name = data.get("name")
        self.teacher_count = data.get("teacher_count")
        self.problem_count = data.get("problem_count")
        self.organization_count = data.get("organization_count")
        self.user_count = data.get("user_count")
        self.course_count = data.get("course_count")
        self.knowledge_point_count = data.get("knowledge_point_count")
        self.problem_set_count = data.get("problem_set_count")





@dataclass
class Statics:
    site_statistics: SiteStatistics

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.site_statistics = SiteStatistics(data.get("site_statistics"))




