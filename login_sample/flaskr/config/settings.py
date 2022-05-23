import os


class DevelopmentConfig:
    dir_path = os.path.dirname(__file__)
    # print(dir_path)
    basedir = os.path.normpath(os.path.join(dir_path, "..\.."))
    print(basedir)
    SECRET_KEY = "mysite"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        basedir, "data_development.sqlite"
    )
    print(SQLALCHEMY_DATABASE_URI)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENV = "development"


class ProductionConfig:
    dir_path = os.path.dirname(__file__)
    # print(dir_path)
    basedir = os.path.normpath(os.path.join(dir_path, "..\.."))
    print(basedir)
    SECRET_KEY = "mysite"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        basedir, "data_production.sqlite"
    )
    print(SQLALCHEMY_DATABASE_URI)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENV = "production"
