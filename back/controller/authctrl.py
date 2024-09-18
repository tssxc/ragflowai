from flask import g
from flask_httpauth import HTTPBasicAuth, MultiAuth
from sqlalchemy import or_

from back.models import User, db

basic_auth = HTTPBasicAuth()


@basic_auth.verify_password
def verify_password(username, password):
    """
    验证账号密码
    :param username:
    :param password:
    :return:
    """
    if not all((username, password)):
        return False
    else:
        user = User.query.filter(or_(User.username == username)).first()
        if not user:
            return False
        g.user = user
        return True


class PostUserCtrl:

    @staticmethod
    def username_exists(username):
        return User.query.filter_by(username=username).one_or_none()  # 返回一条记录或者None

    @staticmethod
    def new_user(username, password):
        """
        创建新用户
        :param username:
        :param password:
        :return:
        """
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return user
