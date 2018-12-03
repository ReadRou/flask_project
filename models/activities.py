import datetime

from mongoengine import *

from core import db


class SignIn(db.Document):
    """签到记录表"""
    id = StringField(primary_key=True)
    user_id = StringField(unique=True)
    last_sign_day = DateField()  # 上次签到日
    sign_days = StringField(max_length=100, default='[]')  # 当月签到日列表
    multi_sign_bonus = StringField(max_length=15, default='[]')  # 累计签到奖励领取列表
    created = DateTimeField(default=datetime.datetime.now())

    def __init__(self, user_id, last_sign_day, sign_days):
        self.user_id = user_id
        self.last_sign_day = last_sign_day
        self.sign_days = sign_days


class BindPhoneActivity(db.Model):
    """绑定手机送288阅币活动"""
    id = StringField(primary_key=True)
    user_id = StringField(unique=True)
    created = DateTimeField(default=datetime.datetime.now())

    def __init__(self, user_id):
        self.user_id = user_id
