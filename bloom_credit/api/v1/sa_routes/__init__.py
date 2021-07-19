# API design:
# http://stackoverflow.com/questions/28795561/support-multiple-api-versions-in-flask
from flask import Blueprint

api_v1 = Blueprint('api_v1_blueprint', __name__)

# New sa_routes should be be imported here
from . import (
    consumer,
)
