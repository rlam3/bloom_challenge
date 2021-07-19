# -*- coding: utf-8 -*-

#######################
####### imports #######
#######################

from bloom_credit.models.consumer import Consumer
from bloom_credit.models.credit_tag import CreditTag
from bloom_credit.models.consumer_tag_score import ConsumerTagScore

from flask import (
    Flask,
    current_app,
    request,
    g,
    # current_user,
)
from bloom_credit.extensions import (
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
    DB_NAME = 'bloom3'
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

    register_shellcontext(app)
    register_api_extensions(app)
    register_api_blueprints(app)

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

        return {
            'app': app,
            'db': db,
            'Consumer': Consumer,
            'CreditTag': CreditTag,
            'ConsumerTagScore': ConsumerTagScore
        }

    app.shell_context_processor(shell_context)


def register_api_blueprints(app):

    from .api.v1.sa_routes import api_v1 as api_v1_blueprint
    app.register_blueprint(api_v1_blueprint, url_prefix='/api/v1')
