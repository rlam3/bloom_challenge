from flask import jsonify
from sqlalchemy.orm import backref
from bloom_credit.extensions import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

# The first line of the file is the header. The structure of the credit records is as follows:
# ● consumer name (string, width = 72)
# ● social security number (integer, width = 9)


class Consumer(db.Model):
    """
    A consumer is a person who has a credit card.
    """
    __tablename__ = "consumer"

    uuid = db.Column(UUID(as_uuid=True), primary_key=True,
                     default=uuid.uuid4)
    ssn = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(72), nullable=False)

    @classmethod
    def get_where_id(cls, uuid):
        return cls.query.get(uuid)

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
        return "<Consumer: {}>".format(self.__dict__)
