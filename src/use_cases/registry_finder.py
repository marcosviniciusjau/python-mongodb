from src.errors.types.not_found import NotFoundError
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse
from src.models.interfaces.orders_repos import OrderReposInterface

from src.errors.error_handler import error_handler
class RegistryFinder:
  def __init__(self, order_repos: OrderReposInterface) -> None:
    self.__order_repos = order_repos

  def find(self,http_request: HttpRequest) -> HttpResponse:
     try:
      order_id = http_request.params['order_id']
      order = self.__search_order(order_id)
      return self.__format_response(order)
     except Exception as exception:
          return error_handler(exception)

  def __search_order(self,order_id:str) -> dict:
      order =  self.__order_repos.select_by_object_id(order_id)
      if not order:
        raise NotFoundError("Pedido não encontrado")
      return order
  def __format_response(self,order: dict) -> HttpResponse:
    order["_id"] = str(order["_id"])
    return HttpResponse(
      body={
      "data": {
        "count": 1,
        "type": "Order",
        "attributes": order
       }
      }, 
      status_code=200
    )