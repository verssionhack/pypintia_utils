from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Bindings:

    def __init__(self, data: dict | None):
        if data is None:
            return None





@dataclass
class Organization:
    id: str
    name: str
    code: str
    type: str
    logo: str

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.id = data.get("id")
        self.name = data.get("name")
        self.code = data.get("code")
        self.type = data.get("type")
        self.logo = data.get("logo")





@dataclass
class StudentUsers:
    id: str
    student_number: str
    name: str
    user_id: str
    image: str
    organization: Organization

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.id = data.get("id")
        self.student_number = data.get("student_number")
        self.name = data.get("name")
        self.user_id = data.get("user_id")
        self.image = data.get("image")
        self.organization = Organization(data.get("organization"))





@dataclass
class Account:
    id: str
    type: str

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.id = data.get("id")
        self.type = data.get("type")





@dataclass
class UserAccount:
    account: Account
    balance: int

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.account = Account(data.get("account"))
        self.balance = data.get("balance")





@dataclass
class UserRewardAccount:
    account: Account
    balance: int

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.account = Account(data.get("account"))
        self.balance = data.get("balance")





@dataclass
class UsersProfile:
    bindings: Bindings
    student_users: List[StudentUsers]
    user_account: UserAccount
    user_reward_account: UserRewardAccount

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.bindings = Bindings(data.get("bindings"))
        self.student_users = [StudentUsers(i) for i in (data.get("student_users") if data.get("student_users") is not None else [])]
        self.user_account = UserAccount(data.get("user_account"))
        self.user_reward_account = UserRewardAccount(data.get("user_reward_account"))




