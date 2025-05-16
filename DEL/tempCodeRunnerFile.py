from abc import ABC, abstractmethod

class payments(ABC):
    def database(self):
        print("connected to a database")
        
    @abstractmethod
    def pay(self,amount):
        pass
    
    
class bank(payments):
    def transaction(self):
        print("Tranction !!")
        
    def pay(self,amount):
        print("this is system done")
        
b = bank()
b.transaction()