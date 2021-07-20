from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from ..extensions import db

from sqlalchemy.dialects.postgresql import UUID
import uuid

from .saBase import Base

# from .consumer import Consumer

# The first line of the file is the header. The structure of the credit records is as follows:
# ● consumer name (string, width = 72)
# ● social security number (integer, width = 9)

from sqlalchemy.dialects.postgresql import UUID


class ConsumerTagScore(Base):
    """
    A consumer is a person who has a credit card.
    """
    __tablename__ = "consumer_tag_score"

    score = db.Column(db.Integer, nullable=False)

    # relationship to the Consumer table
    consumer_id = db.Column(db.ForeignKey(
        'consumer.uuid'), nullable=False, primary_key=True)

    # relationship to credit tag table
    credit_tag_id = db.Column(db.ForeignKey(
        'credit_tag.id'), nullable=False, primary_key=True)
