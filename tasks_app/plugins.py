"""Plugins module."""

# Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Local applications
from .config import Config


def create_app():
    """Create, set, and return a Flask instance."""
    app = Flask(__name__)
    app.config.from_object(Config)
    return app


app = create_app()
db = SQLAlchemy(app)
