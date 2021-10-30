import flask
from flask import Blueprint
from flask_expects_json import expects_json

import schemas


categorizer_view = Blueprint('categorizer_view', __name__)

@categorizer_view.route("/v1/categorize", methods=["POST"])
@expects_json(schemas.CATEGORIZE_PRODUCT)
def categorize_product():
    request_body = flask.request.json
    products = request_body.get("products")

    print(request_body, flush=True)
    return "yes :)"
