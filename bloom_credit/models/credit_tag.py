from flask_sqlalchemy import SQLAlchemy
from ..extensions import db


class CreditTag(db.Model):
    """
    A consumer is a person who has a credit card.
    """
    __tablename__ = "credit_tag"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(5), nullable=False)

    @classmethod
    def get_where(cls, **kwargs):
        return cls.query.filter_by(**kwargs)

    @classmethod
    def create(cls, commit=True, **kwargs):
        instance = cls(**kwargs)
        return instance.save(commit=commit)

    # Save the consumer to the database
    def save(self, commit=True):
        db.session.add(self)
        db.session.flush()
        if commit:
            db.session.commit()
        return self

    def __repr__(self):
        return "<CreditTag: {}>".format(self.__dict__)


# class ConsumerTags(db.Model):
#     """
#     A consumer tag is a tag that is assigned to a consumer.
#     """
#     __tablename__ = "consumer_tags"

#     tag_id = db.Column(db.Integer, primary_key=True, nullable=False)
#     tag = db.Column(db.String(72), nullable=False)

#     def __repr__(self):
#         return "<ConsumerTag: {}>".format(self.tag)
