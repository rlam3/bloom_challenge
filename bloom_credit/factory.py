# -*- coding: utf-8 -*-

#######################
####### imports #######
#######################

from flask import (
    Flask,
    current_app,
    request,
    g,
)
from .extensions import (
    db,
    migrate,
    marshmallow
)

import os
import sys
basedir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(basedir)


class AppConfigs(object):
    """Configurations for Flask App. 
    Postgresql Sqlalchemy configurations
    """
    DEBUG = True
    TESTING = True

    # Databse - Self hosted on main app
    DB_HOST = 'localhost'
    DB_PORT = 5432
    DB_NAME = 'bloom'
    DB_USERNAME = ''
    DB_PASSWORD = ''

    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SQLALCHEMY_DATABASE_URI = 'postgresql://'+DB_USERNAME + \
        ':'+DB_PASSWORD+'@'+DB_HOST+':'+str(DB_PORT)+'/'+DB_NAME


__all__ = ['create_app']


def create_before_request(app):
    def before_request():
        g.db = db
    return before_request


def create_app(config_object=None,
               for_api=False):
    """
    In order to differentiate the app creation between
    Dev, Prod, Testing, Staging
    We must pass int the proper config_oject
    to create_app via CURRENT_ENV of system
    """

    app = Flask(__name__)

    app.config.from_object(AppConfigs())

    register_api_extensions(app)
    register_api_blueprints(app)

    register_shellcontext(app)

    app.before_request(create_before_request(app))

    return app


def register_api_extensions(app):

    db.init_app(app)
    migrate.init_app(app, db)

    marshmallow.init_app(app)

    return None


def register_shellcontext(app):
    """Register shell context objects."""
    def shell_context():
        """Shell context objects."""

        from .models.consumer import Consumer

        return {
            'app': app,
            'db': db,
            'Consumer': Consumer,
        }

    app.shell_context_processor(shell_context)


def register_api_blueprints(app):

    pass
