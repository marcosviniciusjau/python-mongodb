from datetime import datetime

from flask import jsonify
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse
from src.models.interfaces.orders_repos import OrderReposInterface

class RegistryOrder:
  def __init__(self, order_repos: OrderReposInterface):
    self.__order_repos = order_repos

  def registry(self,http_request: HttpRequest) -> HttpResponse:
    try:
      body = http_request.body
      new_order = self.__format_new_order(body)
      self.__registry_order(new_order)

      return self.__format_response()
    except Exception as exception:
      return HttpResponse(
        body = {"error": str(exception)},
        status_code = 400
      )
  
  def __format_new_order(self,body: dict) -> dict:
    new_order = body["data"]
    new_order = { **new_order, "created_at": datetime.now()}
    return new_order
  
  def __registry_order(self,new_order: dict) -> None:
     self.__order_repos.insert_order(new_order)

  def __format_response(self) -> dict:
    return HttpResponse(
      body={
      "data": {
        "type": "Order",
        "count": 1,
        "registry": True
       }
      }, 
      status_code=201
    )