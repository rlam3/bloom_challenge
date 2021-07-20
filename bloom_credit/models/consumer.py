from sqlalchemy.orm import backref
from ..extensions import db

from sqlalchemy.dialects.postgresql import UUID
import uuid
from .consumer_tag_score import ConsumerTagScore
from .saBase import Base

# The first line of the file is the header. The structure of the credit records is as follows:
# ● consumer name (string, width = 72)
# ● social security number (integer, width = 9)


class Consumer(Base):
    """
    A consumer is a person who has a credit card.
    """
    __tablename__ = "consumer"

    uuid = db.Column(UUID(as_uuid=True), primary_key=True,
                     default=uuid.uuid4)
    ssn = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(72), nullable=False)

    # One to many credit tag scores
    consumer_tag_scores = db.relationship(
        'ConsumerTagScore', backref='consumer', lazy='dynamic')
