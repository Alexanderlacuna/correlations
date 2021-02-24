SQLALCHEMY_DATABASE_URI = "mysql://kabui:1234@localhost/test"

from flask import Flask
# from db_setup import db

class Config:
	Testing= False
class DevConfig(Config):
    Testing = True
    # SQLALCHEMY_DATABASE_URI = "mysql://kabui:1234@localhost/test"
    # SQLALCHEMY_DATABASE_URI ="mysql+pymysql://root:1234@localhost/test"
    SECRET_KEY = "password"
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def get_config():
    return {
        "dev": DevConfig
    }


def create_app(config):
	app = Flask(__name__)
	configs = get_config()
	app.config.from_object(configs["dev"])
	return app