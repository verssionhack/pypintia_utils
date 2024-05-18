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




    def __init__(self, data: dict):

        self.gender = data.get('gender')
        self.phone = data.get('phone')
        self.zip_code = data.get('zip_code')
        self.student_id = data.get('student_id')
        self.graduated = data.get('graduated')
        self.first_name = data.get('first_name')
        self.last_name = data.get('last_name')
        self.image = data.get('image')
        self.intention = data.get('intention')
        self.skill = data.get('skill')



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




    def __init__(self, data: dict):

        self.id = data.get('id')
        self.email = data.get('email')
        self.nickname = data.get('nickname')
        self.fake = data.get('fake')
        self.roles = data.get('roles')
        self.organization_id = data.get('organization_id')
        self.is_organization_admin = data.get('is_organization_admin')
        self.organization_subdomain = data.get('organization_subdomain')
        self.detail = Detail(data.get('detail'))
        self.info = data.get('info')
        self.activate = data.get('activate')
        self.phone = data.get('phone')
        self.real_name = data.get('real_name')
        self.banned = data.get('banned')
        self.deregistered = data.get('deregistered')



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




    def __init__(self, data: dict):

        self.union_id = data.get('union_id')
        self.nickname = data.get('nickname')
        self.gender = data.get('gender')
        self.city = data.get('city')
        self.province = data.get('province')
        self.country = data.get('country')
        self.image = data.get('image')
        self.open_id = data.get('open_id')



@dataclass
class UserPacket:
    user: User
    email_login: bool
    oms_login: bool
    student_user_login: bool
    wechat_user: WechatUser
    phone_login: bool
    course_group_internal_user_id: str




    def __init__(self, data: dict):

        self.user = User(data.get('user'))
        self.email_login = data.get('email_login')
        self.oms_login = data.get('oms_login')
        self.student_user_login = data.get('student_user_login')
        self.wechat_user = WechatUser(data.get('wechat_user'))
        self.phone_login = data.get('phone_login')
        self.course_group_internal_user_id = data.get('course_group_internal_user_id')



