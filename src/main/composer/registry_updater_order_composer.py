from src.use_cases.registry_updater import RegistryUpdater
from src.models.repos.order_repos import OrderRepos
from src.models.connection.connection_handler import db_connection_handler

def registry_updater_order_composer():
  conn = db_connection_handler.get_connection() 
  model = OrderRepos(conn)
  use_case = RegistryUpdater(model)

  return use_case