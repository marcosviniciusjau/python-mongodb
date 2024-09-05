class OrderRepos:
  def __init__(self, db_connection) -> None:
    self.__collection_name = "orders"
    self.__db_connection = db_connection

  def get_orders(self):
    pass

  def get_order(self):
    pass

  def create_order(self, document: dict)-> None:
    collection = self.__db_connection.get_connection()[self.__collection_name]
    collection.insert_one(document)

def insert_list_orders(self, list_documents: list) -> None:
    collection = self.__db_connection.get_connection()[self.__collection_name]
    collection.insert_many(list_documents)

def select_many(self, filter: dict) -> list:
    collection = self.__db_connection.get_connection()[self.__collection_name]
    data = collection.find(filter)
    return data

def select_one(self, filter: dict) -> dict:
    collection = self.__db_connection.get_connection()[self.__collection_name]
    response = collection.find_one(filter)
    return response