from flask import Flask, jsonify, request, abort, blueprints

# Create a REST API endpoint for retrieving the full set of credit tags
# for a given consumer by consumer id provided as a query-string parameter.
# The endpoint should return data in JSON format.

from . import api_v1 as api_v1_blueprint
from bloom_challenge.bloom_credit.models.consumer import Consumer
from bloom_challenge.bloom_credit.models.credit_tag import CreditTag
from bloom_challenge.bloom_credit.models.consumer_tag_score import ConsumerTagScore

from ..ma_schema.consumer_schema import ConsumerSchema as consumerSchemaForAPI
from ..ma_schema.consumertagscore_schema import ConsumerTagScoreSchema as consumerTagScoreSchemaForAPI

# create GET route for blueprints to retrieves


@api_v1_blueprint.route('/consumer', methods=['GET'])
def get_consumer_data():

    con = Consumer.get_where_id(request.args.get('consumer_id'))

    consumer_schema = consumerSchemaForAPI()
    result = consumer_schema.dump(con)

    return result


@api_v1_blueprint.route('/consumer/credit_data', methods=['GET'])
def get_consumer_credit_data():

    data = ConsumerTagScore.get_where(
        consumer_id=request.args.get('consumer_id')).all()

    schema = consumerTagScoreSchemaForAPI(many=True)
    return {
        "data": schema.dump(data)
    }
