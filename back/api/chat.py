from flask import jsonify, request
from flask_restful import Resource

from back.controller.chatctrl import get_chats, get_all_chats, new_message
from .utils import jsonify_with_args


class ChatApi(Resource):
    """
    聊天记录
    """

    def __init__(self):
        self.response_obj = {'success': True, 'code': 0, 'data': None, 'msg': ''}

    def get(self, list_id):
        """
        获取聊天记录
        :param list_id:
        :return:
        """
        data = dict()
        messages = get_chats(list_id)
        count = 0
        for message in messages:
            content = message.content
            timestamp = message.timestamp
            data[count] = {
                'content': content,
                'timestamp': timestamp
            }
            count += 1
        self.response_obj['data'] = data
        return jsonify(self.response_obj)

    def post(self):
        """
        新建消息
        :return:
        """
        json_data = request.json
        user_id = json_data.get('user_id')
        content = json_data.get('content')
        list_id = json_data.get('list_id')
        message = new_message(user_id, content, list_id)
        list_id = message.list_id
        user_id = message.user_id
        content = message.content
        data = {
            'list_id': list_id,
            'user_id': user_id,
            'content': content
        }

        self.response_obj['data'] = data
        return jsonify_with_args(self.response_obj, 201)

    def delete(self):
        pass


class ChatListApi(Resource):

    def __init__(self):
        self.response_obj = {'success': True, 'code': 200, 'data': None, 'msg': ''}

    def get(self, user_id):
        """
        获取用户所有对话
        :param user_id:
        :return:
        """
        data = dict()
        chatlists = get_all_chats(user_id)
        count = 0
        for chatlist in chatlists:
            list_id = chatlist.list_id
            data[count] = list_id
            count += 1
        self.response_obj['data'] = data
        return jsonify(self.response_obj)

    def post(self):
        """
        新建会话
        :return:
        """
        pass

    def delete(self):
        pass

