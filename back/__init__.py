from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
#from flask_uploads import configure_uploads, patch_request_class

from back.config import config
from .models import db
from back.api import api_bp, api, users,chat


cors = CORS(resources={r"/api/*": {"orgins": "*"}})

def add_api():
    """
    添加api
    :return:
    """
    api.add_resource(users.UserApi, '/api/register', '/api/users', '/api/users/<int:id>')
    api.add_resource(chat.ChatApi, '/api/chat')


def add_bluprints(app):
    """
    添加蓝图
    :param app:
    :return:
    """
    app.register_blueprint(api_bp)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    cors.init_app(app)
    db.init_app(app)
    migrate = Migrate(app, db)
    #configure_uploads(app, uploads.image_upload)图片上传
    #redis_store.init_app(app)
    add_api()
    api.init_app(app)
    add_bluprints(app)
    return app