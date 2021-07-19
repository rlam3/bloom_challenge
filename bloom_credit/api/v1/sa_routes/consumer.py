from flask import Flask, jsonify, request, abort, blueprints

# Create a REST API endpoint for retrieving the full set of credit tags
# for a given consumer by consumer id provided as a query-string parameter.
# The endpoint should return data in JSON format.

# create a blueprint for api v1
# api_v1 = blueprints.Blueprint('api_v1', __name__)
from . import api_v1 as api_v1_blueprint

from bloom_challenge_x.bloom_credit.models.consumer import Consumer

from ..ma_schema.consumer_schema import ConsumerSchema as consumerSchemaForAPI


@api_v1_blueprint.route('/consumer', methods=['GET'])
def get_consumer_data():

    con = Consumer.get_where_id(request.args.get('consumer_id'))

    consumer_schema = consumerSchemaForAPI()
    result = consumer_schema.dump(con)

    return result
