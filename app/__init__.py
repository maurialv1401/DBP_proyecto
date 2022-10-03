from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import LoginManager


app = Flask(__name__)
cors = CORS(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

from app import models, topRoutes
'''
from app.routes.login_bp import login_bp
from app.routes.user_bp import user_bp

app.register_blueprint(login_bp, url_prefix="/login")
app.register_blueprint(user_bp, url_prefix="/user")
'''
db.create_all()