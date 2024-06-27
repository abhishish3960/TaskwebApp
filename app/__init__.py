# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from flask_migrate import Migrate
from flask_cors import CORS
# Initialize Flask application
app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

# Initialize SQLAlchemy
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# Import routes here to avoid circular import
from app import routes, models
