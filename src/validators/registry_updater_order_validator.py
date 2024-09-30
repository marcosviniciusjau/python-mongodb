from cerberus import Validator
from src.errors.types.unprocessable_entity import UnprocessableEntityError
def registry_updater_order_validator(body: any):
   body_validator = Validator({
     "data": {
        "type": "dict",
        "schema": {
           "name": {"type": "string"},
           "address": {"type": "string"},
           "cupom": {"type": "boolean"},
        }
     }
   })

   response = body_validator.validate(body)
   if response is False:
      raise UnprocessableEntityError(body_validator.errors)