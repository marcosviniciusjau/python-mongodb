from flask import Blueprint, jsonify, request
from src.main.http_types.request import Request
delivery_routes_bp = Blueprint("delivery_routes", __name__)

@delivery_routes_bp.route("/delivery/order", methods=["POST"])
def registry_order():
    print(request.json)
    request = Request(body=request.json)
    return jsonify({"ola": "Mundo"}),200
