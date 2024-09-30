from src.errors.types.not_found import NotFoundError
from src.errors.types.unprocessable_entity import UnprocessableEntityError
from src.main.http_types.http_response import HttpResponse

def error_handler(error: Exception) -> HttpResponse:
  if isinstance(error, (NotFoundError,UnprocessableEntityError)):
    return HttpResponse(
      status_code= error.status_code,
      body={
        "errors": [{
          "title": error.name,
          "detail": error.message
        }]
      }
    )
  
  return HttpResponse(
    status_code= 500,
    body={
      "errors": [{
        "title": "InternalServerError",
        "detail": str(error)
      }]
    }
  )
  