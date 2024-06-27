from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from app.config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize plugins
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    # Import and register blueprints
    from app.routes import tasks_bp
    app.register_blueprint(tasks_bp)

    # Import models (if needed)
    from app import models

    return app, db
