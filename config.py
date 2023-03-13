import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or \
        "a very complcated secret key 1234."
    SQLALCHEMY_TRACK_MODIFICATION = False

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URL") or \
        "sqlite:///" + os.path.join(basedir, "data/data-dev.sqlite")
    DEBUG = True


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("PROD_DATABASE_URL") or \
        "sqlite:///" + os.path.join(basedir, "data/data.sqlite")


config = {
    "dev": DevConfig,
    "prod": ProdConfig,

    "default": DevConfig,
}
