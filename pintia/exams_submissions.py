from dataclasses import dataclass
from typing import *

@dataclass
class ExamsSubmissions:
    submission_id: str

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.submission_id = data.get("submission_id")




