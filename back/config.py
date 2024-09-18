import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'supersecretkey'

    FLASK_POSTS_PRT_PAGE = '10'
    #上传图片
    #
    def __init__(self):
        pass

    @staticmethod
    def init_app(app):
        pass

class MySQLConfig:
    MYSQL_USERNAME = 'root'
    MYSQL_PASSWORD = '123456'
    MYSQL_DB = 'ragflow'
    MYSQL_HOST = 'localhost:3306'

class DevelopmentConfig(Config):
    DEBUG = True
    #database = MySQLConfig.MYSQL_DB
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MySQLConfig.MYSQL_USERNAME}:{MySQLConfig.MYSQL_PASSWORD}'\
                              f'@{MySQLConfig.MYSQL_HOST}/{MySQLConfig.MYSQL_DB}'


class TestingConfig(Config):
    TESTING = True
    MYSQL_DB = 'test'

class ProductionConfig(Config):
    database = '123'

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

