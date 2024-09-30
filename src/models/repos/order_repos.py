from bson import ObjectId
from src.models.interfaces.orders_repos import OrderReposInterface

class OrderRepos(OrderReposInterface):
    def __init__(self, db_connection) -> None:
        self.__collection_name = "orders"
        self.__db_connection = db_connection
     
    def insert_order(self, document: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)

    def insert_list_orders(self, list_documents: list) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_many(list_documents)

    def select_many(self, filter: dict) -> list:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(filter)
        return list(data)

    def select_one(self, filter: dict) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one(filter)
        return response

    def select_if_props_exists(self) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one({"address": {"$exists": True}})
        return response

    def select_by_object_id(self, object_id: str) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one({"_id": ObjectId(object_id)})
        return response

    def edit_registry(self, order_id:str, update_fields: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one(
            {"_id": ObjectId(order_id)},
            {"$set": update_fields}
        )

    def edit_many_registries(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_many(
            {"items.refrigerante": {"$exists": True}},
            {"$set": {"items.refrigerante.quantidade": 30}}
        )
    def edit_many_registry_with_increment(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one(
            {"_id": ObjectId("66d9c123a0015322e677517c")},
            {"$inc": {"items.refrigerante.quantidade": 3}}
        )

    def delete_registry(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.delete_one({"_id": ObjectId("66d9c123a0015322e677517c")})

    def delete_many_registries(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.delete_many({"items.refrigerante.quantidade": 30})
