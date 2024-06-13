from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    time = db.Column(db.String(20), nullable=False)
    image = db.Column(db.String(200))  # Optional field for Pro license

    def __repr__(self):
        return f'<Todo {self.title}>'
