from dataclasses import dataclass
from typing import *

@dataclass
class Detail:
    gender: str
    phone: str
    mfa: list
    zip_code: str
    student_id: str
    graduated: bool
    first_name: str
    last_name: str
    schools: list
    experiences: list
    image: str
    intention: str
    skill: str
    location: list

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.gender = data.get("gender")
        self.phone = data.get("phone")
        self.mfa = data.get("mfa")
        self.zip_code = data.get("zip_code")
        self.student_id = data.get("student_id")
        self.graduated = data.get("graduated")
        self.first_name = data.get("first_name")
        self.last_name = data.get("last_name")
        self.schools = data.get("schools")
        self.experiences = data.get("experiences")
        self.image = data.get("image")
        self.intention = data.get("intention")
        self.skill = data.get("skill")
        self.location = data.get("location")





@dataclass
class User:
    id: str
    email: str
    nickname: str
    fake: bool
    roles: List[str]
    organization_id: str
    is_organization_admin: bool
    organization_subdomain: str
    detail: Detail
    info: str
    activate: bool
    phone: str
    real_name: str
    banned: bool
    deregistered: bool

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.id = data.get("id")
        self.email = data.get("email")
        self.nickname = data.get("nickname")
        self.fake = data.get("fake")
        self.roles = [str(i) for i in (data.get("roles") if data.get("roles") != None else [])]
        self.organization_id = data.get("organization_id")
        self.is_organization_admin = data.get("is_organization_admin")
        self.organization_subdomain = data.get("organization_subdomain")
        self.detail = Detail(data.get("detail"))
        self.info = data.get("info")
        self.activate = data.get("activate")
        self.phone = data.get("phone")
        self.real_name = data.get("real_name")
        self.banned = data.get("banned")
        self.deregistered = data.get("deregistered")





@dataclass
class StudentUser:
    id: str
    student_number: str
    name: str
    user_id: str
    image: str

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.id = data.get("id")
        self.student_number = data.get("student_number")
        self.name = data.get("name")
        self.user_id = data.get("user_id")
        self.image = data.get("image")





@dataclass
class WechatUser:
    union_id: str
    nickname: str
    gender: int
    city: str
    province: str
    country: str
    image: str
    open_id: str

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.union_id = data.get("union_id")
        self.nickname = data.get("nickname")
        self.gender = data.get("gender")
        self.city = data.get("city")
        self.province = data.get("province")
        self.country = data.get("country")
        self.image = data.get("image")
        self.open_id = data.get("open_id")





@dataclass
class Organization:
    id: str
    name: str
    comment: str
    code: str
    country: str
    type: str
    subdomain: str
    logo: str
    vip_type: str

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.id = data.get("id")
        self.name = data.get("name")
        self.comment = data.get("comment")
        self.code = data.get("code")
        self.country = data.get("country")
        self.type = data.get("type")
        self.subdomain = data.get("subdomain")
        self.logo = data.get("logo")
        self.vip_type = data.get("vip_type")





@dataclass
class CourseGroup:
    id: str
    name: str
    internal_user_id: str
    owner_id: str
    organization_id: str

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.id = data.get("id")
        self.name = data.get("name")
        self.internal_user_id = data.get("internal_user_id")
        self.owner_id = data.get("owner_id")
        self.organization_id = data.get("organization_id")





@dataclass
class UserCurrent:
    user: User
    email_login: bool
    oms_login: bool
    student_user_login: bool
    student_user: StudentUser
    wechat_user: WechatUser
    phone_login: bool
    course_group_id: str
    organization: Organization
    course_group: CourseGroup
    course_group_permission: str

    def __init__(self, data: dict | None):
        if data is None:
            return None
        self.user = User(data.get("user"))
        self.email_login = data.get("email_login")
        self.oms_login = data.get("oms_login")
        self.student_user_login = data.get("student_user_login")
        self.student_user = StudentUser(data.get("student_user"))
        self.wechat_user = WechatUser(data.get("wechat_user"))
        self.phone_login = data.get("phone_login")
        self.course_group_id = data.get("course_group_id")
        self.organization = Organization(data.get("organization"))
        self.course_group = CourseGroup(data.get("course_group"))
        self.course_group_permission = data.get("course_group_permission")




