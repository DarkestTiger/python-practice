from flask import SQLAlchemy
from myproject import create_app
db = SQLAlchemy()

class User(db.model):
  __table_name__ = 'user'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  username = db.Column(db.String(10), nullable=False)
  password = db.Column(db.String(20), nullable=False)

