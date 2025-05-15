# #Inheritance allows us to define a class that inherits all the methods and properties from another class.
# class A:


#     def __init__(self,name):
#         self.name = name
        
        
#     def speak(self):
#         pass
    
    
# class B(A):
#     def speak(self):
#         print(f"Hello {self.name}")
        
        
# b = B("sachin")
# b.speak()


#single inheritance
class A:
    def __init__(self,name):
        self.name = name
        
class B(A):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age


c= B("Sachin",20)
print(c.name)
print(c.age)