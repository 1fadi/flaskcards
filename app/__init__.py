from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask_moment import Moment

from .filters import ifchanged
from config import config

bootstrap = Bootstrap5()
db = SQLAlchemy()
moment = Moment()


def create_app(config_):
    app = Flask(__name__)
    app.config.from_object(config[config_])
    app.jinja_env.filters['ifchanged'] = ifchanged

    config[config_].init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    moment.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
