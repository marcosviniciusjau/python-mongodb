from bson import ObjectId


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

    def select_many_with_props(self, filter: dict) -> list:
      collection = self.__db_connection.get_connection()[self.__collection_name]
      data = collection.find(filter)
      return data

    def select_if_props_exits(self) -> dict:
      collection = self.__db_connection.get_connection()[self.__collection_name]
      response = collection.find_one({"address": {"$exists": True}})
      return response

    def select_by_object_id(self,object_id:str)->dict:
      collection = self.__db_connection.get_connection()[self.__collection_name]
      response = collection.find_one({"_id": ObjectId(object_id)})
      return response

    def edit_registry(self)->None:
      collection = self.__db_connection.get_connection()[self.__collection_name]
      collection.update_one(
        {"_id": ObjectId("66d9c123a0015322e677517c")},
        {"$set": {"cupom": True}}
      )

    def edit_many_registries(self)->None:
      collection = self.__db_connection.get_connection()[self.__collection_name]
      collection.update_many(
        {"items.refrigerante": {"$exists": True}},
        {"$set": {"items.refrigerante.quantidade": 30}}
      )

    def edit_many_registry_with_increment(self)->None:
      collection = self.__db_connection.get_connection()[self.__collection_name]
      collection.update_one(
        {"_id": ObjectId("66d9c123a0015322e677517c")},
        {"$inc": {"items.refrigerante.quantidade": 3}}
      )

    def delete_registry(self)->None:
      collection = self.__db_connection.get_connection()[self.__collection_name]
      collection.delete_one({"_id": ObjectId("66d9c123a0015322e677517c")})

    def delete_many_registries(self)->None:
      collection = self.__db_connection.get_connection()[self.__collection_name]
      collection.delete_many({"$set": {"items.refrigerante.quantidade": 30}})