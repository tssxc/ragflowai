from flask import jsonify, request, g
from flask_restful import Resource

from back.models import User
from .utils import jsonify_with_args
from back.controller.authctrl import basic_auth, PostUserCtrl

user_ctrl = PostUserCtrl()

'''def abort_if_net_exist(user_id):
    """
    确认用户存在，否则返回404
    :param user_id:
    :return:
    """
    desc = 'The user {} not exist.'.format(user_id)
    user = User.Query.get_or_404(user_id, description=desc)
    return user'''


class UserApi(Resource):
    """
    创建获取用户信息
    """

    def __init__(self):
        self.response_obj = {'success': True, 'code': 0, 'data': None, 'msg': ''}

    @basic_auth.login_required
    def get(self, user_id=None):
        data = dict()
        if user_id:
            desc = f'The user {user_id} not exist.'
            user = User.query.get_or_404(user_id, description=desc)
        else:
            user = g.user
        if user:
            data['username'] = user.username
            data['id'] = user.id
            self.response_obj['data'] = data
            return jsonify(self.response_obj)
        else:
            self.response_obj['code'] = 1
            self.response_obj['success'] = False
            return jsonify_with_args(self.response_obj, 400)

    def post(self):
        """
        注册新用户
        :return:
        """
        json_data = request.json
        username = json_data.get('username')
        password = json_data.get('password')
        re_password = json_data.get('re_password')
        if not all([username, password]):
            self.response_obj['code'] = 1
            self.response_obj['success'] = False
            self.response_obj['msg'] = 'Missing argument'
            return jsonify_with_args(self.response_obj, 400)
        if password != re_password:
            self.response_obj['code'] = 1
            self.response_obj['success'] = False
            self.response_obj['msg'] = 'Please confirm password has been set correctly.'
            return jsonify_with_args(self.response_obj, 409)
        if user_ctrl.username_exists(username):
            self.response_obj['code'] = 1
            self.response_obj['success'] = False
            self.response_obj['msg'] = 'username already exists'
            return jsonify_with_args(self.response_obj, 409)

        data = dict()
        user = user_ctrl.new_user(username, password)
        user_id = user.id
        username = user.username
        data['user_id'] = user_id
        data['username'] = username
        self.response_obj['data'] = data
        return jsonify_with_args(self.response_obj, 201)
