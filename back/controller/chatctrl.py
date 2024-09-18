
from back.models import Message, ChatList, db


def get_chats(list_id):
    """
    获取对话列表
    :param list_id:
    :return:
    """
    messages = Message.query.filter_by(list_id=list_id).all
    return messages


def get_all_chats(user_id):
    """
    获取所有的对话
    :param user_id:
    :return:
    """
    chatlists = ChatList.query.filter_by(user_id=user_id)
    return chatlists


def new_message(user_id, content, list_id):
    """
    上传消息
    :param user_id:
    :param content:
    :param list_id:
    :return:
    """
    message = Message(user_id=user_id, content=content, list_id=list_id)
    db.session.add(message)
    db.session.commit()
    return message
