from flask import Flask
from extensions import DATABASE_URL
from extensions import db, jwt
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db.init_app(app)
jwt.init_app(app)
app.config['JWT_SECRET_KEY'] = os.environ["SECRET_KEY"]
    

from models import Usuario

with app.app_context():
    # db.drop_all()
    db.create_all()


import routes

