from flask import Flask
from app.config import Config
# app.config = on importe le module config.py
# Config = on importe la classe Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
# db = bdd Fauvel
migrate = Migrate(app, db)

from app import modeles
from app.routes import routes