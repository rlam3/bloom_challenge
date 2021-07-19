from bloom_credit.extensions import marshmallow as ma


class ConsumerSchema(ma.Schema):

    """
    ConsumerSchema for API
    """

    class Meta:

        fields = (
            'uuid',
            'name',
            'ssn'
        )
