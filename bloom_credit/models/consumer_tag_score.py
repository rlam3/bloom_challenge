from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from ..extensions import db

from sqlalchemy.dialects.postgresql import UUID
import uuid

# from .consumer import Consumer

# The first line of the file is the header. The structure of the credit records is as follows:
# ● consumer name (string, width = 72)
# ● social security number (integer, width = 9)

from sqlalchemy.dialects.postgresql import UUID


class ConsumerTagScore(db.Model):
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

    @classmethod
    def create(cls, commit=True, **kwargs):
        instance = cls(**kwargs)
        return instance.save(commit=commit)

    @classmethod
    def get_where(cls, **kwargs):
        return cls.query.filter_by(**kwargs)

    # Save the consumer to the database
    def save(self, commit=True):
        db.session.add(self)
        db.session.flush()
        if commit:
            db.session.commit()
        return self

    def __repr__(self):
        return "<ConsumerTagScore: {}>".format(self.__dict__)
