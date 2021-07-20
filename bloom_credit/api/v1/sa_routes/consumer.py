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

from bloom_credit.api.v1.exception import InvalidAPIUsage

# create GET route for blueprints to retrieves


@api_v1_blueprint.route('/consumer', methods=['GET'])
def get_consumer_data():

    try:

        if request.args.get('consumer_id') is None:
            raise InvalidAPIUsage(
                'consumer_id query-string parameter is required', 400)

        # get consumer id from query string
        con = Consumer.get_where_id(request.args.get('consumer_id'))

        # raise error if no consumer found
        if con is None:
            raise InvalidAPIUsage('consumer not found', 404)

        schema = consumerSchemaForAPI()
        return jsonify(data=schema.dump(con)), 200

    except Exception as e:
        return jsonify(e.to_dict())


@api_v1_blueprint.route('/consumer/credit_data', methods=['GET'])
def get_consumer_credit_data():
    try:

        if request.args.get('consumer_id') is None:
            raise InvalidAPIUsage(
                'consumer_id query-string parameter is required', 400)

        data = ConsumerTagScore.get_where(
            consumer_id=request.args.get('consumer_id')).all()

        if len(data) == 0:
            raise InvalidAPIUsage(
                message='consumer data not found', status_code=400)

        # Return user if no exception is raised
        schema = consumerTagScoreSchemaForAPI(many=True)
        return jsonify(data=schema.dump(data)), 200

    except Exception as e:
        return jsonify(e.to_dict())
