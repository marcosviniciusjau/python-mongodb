from src.models.repos.order_repos import OrderRepos
from src.models.connection.connection_handler import db_connection_handler
from src.use_cases.registry_finder import RegistryFinder

def registry_finder_composer():
  conn = db_connection_handler.get_connection() 
  model = OrderRepos(conn)
  use_case = RegistryFinder(model)

  return use_case