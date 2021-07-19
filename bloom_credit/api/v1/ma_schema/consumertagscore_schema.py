
from bloom_credit.extensions import marshmallow as ma


class ConsumerTagScoreSchema(ma.Schema):

    """
    ConsumerTagScoreSchema for API
    """

    class Meta:

        fields = (
            'score',
            'consumer_id',
            'credit_tag_id'
        )
