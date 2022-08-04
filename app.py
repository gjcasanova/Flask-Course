"""App module."""

# Local applications
from tasks_app.models import User
from tasks_app.plugins import app as tasks_app
from tasks_app.plugins import db

app = tasks_app


@app.before_first_request
def create_tables():
    """Create tables in database."""
    db.create_all()


@app.route('/')
def hello_world():
    """Return a message for testing."""
    user = User(name='Guillermo', username='gjcasanova', password='123')
    db.session.add(user)
    db.session.commit()
    print(user.name, user.username, user.password)
    return 'Hello world! It works!'


if __name__ == '__main__':
    app.run(debug=True)
