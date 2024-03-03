from flask import Flask
import os
import sqlalchemy

a = Flask(__name__)

db = sqlalchemy()

class user:
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserId = db.Column(db.String, nullable=False)
    UserName = db.Column(db.String, nullable=False)
    Email = db.Column(db.String, nullable=False)
    Password = db.Column(db.String, nullable=False)
    Password2 = db.Column(db.String, nullable=False)
    
    def __init__(self,userid,username,email,password,password2):
        self.UserId = userid
        self.UserName = username
        self.Email = email
        self.Password = password
        self.Password2 = password2

with a.app_context():
    db.create_all()

