from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import marshmallow

db = SQLAlchemy()

migrate = Migrate()

marshmallow = Marshmallow()
