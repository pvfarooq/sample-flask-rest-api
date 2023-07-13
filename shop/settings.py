import os
from pathlib import Path
from datetime import timedelta


class DBConfig(object):
    db_type = os.getenv("DB_TYPE", "sqlite")
    user = os.getenv("DB_USER", "root")
    password = os.getenv("DB_PASSWORD", "a-random-password")
    host = os.getenv("DB_HOST", "127.0.0.1")
    port = os.getenv("DB_PORT", "3306")
    db_name = os.getenv("DB_NAME", "shopapp")

    if db_type == "sqlite":
        current_path = Path(__file__).resolve()
        parent_directory = current_path.parent.parent
        db_uri = f"sqlite:///{parent_directory}/{db_name}.sqlite3"
    else:
        db_uri = f"{db_type}://{user}:{password}@{host}:{port}/{db_name}"


class Config(object):
    ENV = "local"
    DEBUG = True
    SECRET_KEY = os.getenv("SECRET_KEY", "a-random-secret-key")
    # SQLALCHEMY
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_URI", DBConfig.db_uri)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "a-random-jwt-secret-key"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)
    JWT_ALGORITHM = "HS256"
