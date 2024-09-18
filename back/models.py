"""
定义表结构
"""
from datetime import datetime

# from flask import current_app
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import or_, event

# from itsdangerous import (TimedJSONWebSignatureSerializers Serializer, BadSignature, SignatureExpired)

# from back.exception import ValidationError

db = SQLAlchemy()


class User(db.Model):
    """
    用户表
    """
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, comment='主键')
    username = db.Column(db.String(64), index=True, unique=True, comment='用户名')
    # name = db.Column(db.String(32), comment='真实姓名')
    password = db.Column(db.String(128), comment='密码')

    def __repr__(self):
        return '<User %r>' % self.username  # 定义打印的类型

    @staticmethod
    def verify():
        pass


class Message(db.Model):
    """
    聊天信息表
    """
    __tablename__ = 'message'
    __table_args__ = {'extend_existing': True}
    message_id = db.Column(db.Integer, primary_key=True, comment='主键')
    user_id = db.Column(db.Integer, nullable=False, comment='送信者id')
    list_id = db.Column(db.Integer, nullable=False, comment='记录id')
    content = db.Column(db.Text, nullable=False, comment='聊天信息')
    timestamp = db.Column(db.TIMESTAMP, default=datetime.utcnow, comment='创建时间')


class ChatList(db.Model):
    """
    聊天记录表
    """
    __tablename__ = 'chat_list'
    __table_args__ = {'extend_existing': True}
    list_id = db.Column(db.Integer, primary_key=True, comment='主键')
    user_id = db.Column(db.Integer, nullable=False, comment='用户id')
    last_message_id = db.Column(db.Integer, nullable=False, comment='会话id')

# event.listens_for(Message, 'after_insert')
