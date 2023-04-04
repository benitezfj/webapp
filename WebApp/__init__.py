import logging
from logging.handlers import RotatingFileHandler

# import os
# from click import echo
# import sqlalchemy as sa

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask.logging import default_handler
from config import Config

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = "main.login"
login_manager.login_message_category = "info"


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # with app.app_context():
    #     from WebApp.models import (
    #         User,
    #         Role,
    #         Farmland,
    #         Crop,
    #         HistoricFarmland,
    #         SoilFarmland,
    #         Unit,
    #     )

    #     db.create_all()
    #     app.logger.info("Initialized the database!")

    # Check if the database needs to be initialized

    # engine = sa.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    # inspector = sa.inspect(engine)

    # if not inspector.has_table("users"):
    #     with app.app_context():
    #         db.drop_all()
    #         from WebApp.models import User, Role, Farmland, Crop, HistoricFarmland, SoilFarmland
    #         db.create_all()
    #         print(db.metadata.tables.keys())
    #         app.logger.info('Initialized the database!')
    # else:
    #     app.logger.info('Database already contains the users table.')

    from WebApp.routes import main

    app.register_blueprint(main)

    if app.config["LOG_WITH_GUNICORN"]:
        gunicorn_error_logger = logging.getLogger("gunicorn.error")
        app.logger.handlers.extend(gunicorn_error_logger.handlers)
        app.logger.setLevel(logging.DEBUG)
    else:
        file_handler = RotatingFileHandler(
            "instance/flask-user-management.log", maxBytes=16384, backupCount=20
        )
        file_formatter = logging.Formatter(
            "%(asctime)s %(levelname)s %(threadName)s-%(thread)d: %(message)s [in %(filename)s:%(lineno)d]"
        )
        file_handler.setFormatter(file_formatter)
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

    # Remove the default logger configured by Flask
    app.logger.removeHandler(default_handler)

    app.logger.info("Starting the Flask User Management App...")

    return app


# def register_cli_commands(app):
#     @app.cli.command('init_db')
#     def initialize_database():
#         """Initialize the database."""
#         db.drop_all()
#         db.create_all()
#         echo('Initialized the database!')

from WebApp import models
