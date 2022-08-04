"""Models module."""

from .plugins import db


class User(db.Model):
    """
    User.

    User model for authentication and authorization tasks.
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    username = db.Column(db.String(50))
    password = db.Column(db.String(256))
