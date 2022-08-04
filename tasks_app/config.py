"""Config module."""

from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


class Config:
    """
    Config.

    Settings to Tasks `App package`.
    """

    SECRET_KEY = 'sadfkjhqwer23412fasd'
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{BASE_DIR / 'database.sqlite'}"
