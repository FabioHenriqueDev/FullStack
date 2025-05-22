from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
import pymysql
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

load_dotenv()

# Dados de conexão (ajuste conforme seu .env)
USER = os.environ["MYSQL_USER"] # MYSQL_USER
PASSWORD = os.environ["MYSQL_PASSWORD"] # MYSQL_PASSWORD
HOST = "localhost"
PORT = "3307"
DB = os.environ['MYSQL_DATABASE'] # MYSQL_DATABASE


# String de conexão
DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"

engine = create_engine(DATABASE_URL)

db = SQLAlchemy()
jwt = JWTManager()
bcrypt = Bcrypt()



