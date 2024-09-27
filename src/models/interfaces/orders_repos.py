from abc import ABC, abstractmethod

class OrderReposInterface(ABC):
    @abstractmethod
    def insert_order(self, document: dict)-> None: pass

    @abstractmethod
    def insert_list_orders(self, list_documents: list) -> None:pass

    @abstractmethod
    def select_many(self, filter: dict) -> list:pass

    @abstractmethod
    def select_one(self, filter: dict) -> dict:pass

    @abstractmethod
    def select_by_object_id(self,object_id:str)->dict:pass

    @abstractmethod
    def edit_registry(self)->None:pass

    @abstractmethod  
    def edit_many_registries(self)->None:pass

    @abstractmethod  
    def edit_many_registry_with_increment(self)->None:pass

    @abstractmethod
    def delete_registry(self)->None:pass
    
    @abstractmethod 
    def delete_many_registries(self)->None:pass
   