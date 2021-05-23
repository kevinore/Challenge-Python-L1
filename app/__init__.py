import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config, REGIONS_API, REGIONS_API_KEY, COUNTRIES_API
from flask_httpauth import HTTPBasicAuth

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
regions_api = REGIONS_API
regions_token = REGIONS_API_KEY
countries_api = COUNTRIES_API


from app import models, routes

