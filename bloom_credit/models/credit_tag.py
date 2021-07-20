from flask_sqlalchemy import SQLAlchemy
from ..extensions import db

from .saBase import Base


class CreditTag(Base):
    """
    A consumer is a person who has a credit card.
    """
    __tablename__ = "credit_tag"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(5), nullable=False)

    # relationship to credit tag score
    credit_tag_score = db.relationship(
        "ConsumerTagScore", backref="credit_tag", lazy=True)
