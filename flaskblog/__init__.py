from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager 


app = Flask(__name__)
app.config['SECRET_KEY'] = '74b49d7fb56c88d8ca04b5828d1b2324f187067e2008f6ed9abc011e7dbe6c55'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db =  SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from flaskblog import routes