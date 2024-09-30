from src.errors.error_handler import error_handler
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse
from src.models.interfaces.orders_repos import OrderReposInterface
from src.validators.registry_updater_order_validator import registry_updater_order_validator

class RegistryUpdater:
  def __init__(self, order_repos: OrderReposInterface) -> None:
    self.__order_repos = order_repos

  def update(self,http_request: HttpRequest) -> HttpResponse:
    try:
      order_id = http_request.params['order_id']
      body = http_request.body
      self.__validate_body(body)

      self.__update_order(order_id, body)
      return self.__format_response(order_id)
    except Exception as exception:
      return error_handler(exception)

  def __validate_body(self,body: dict) -> None:
    registry_updater_order_validator(body)

  def __update_order(self, order_id, body: dict) -> None:
    update_fields = body["data"]
    self.__order_repos.edit_registry(order_id, update_fields)

  def __format_response(self,order_id:str) -> dict:
    return HttpResponse(
      body={
      "data": {
        "order_id": order_id,
        "type": "Order",
        "count": 1
       }
      }, 
      status_code=200
    )