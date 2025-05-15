#static method which does not any arguments of object
# class Student:
#     school="qwerty"
#     age = 20    
    
#     @staticmethod
#     def name():
#         print("Ajaay ka bhaiya ")
        
#     def __init__(self):
#         print("Constructor is called dunder")    
        
# c = Student()
# c.name()        
    
#__init__ is a constructor which is called when an object is created
#static method which does not any arguments of object
class Student:
    school="qwerty"
    age = 20
    id =1121
    
    def __init__(self,school,age,id):
        self.school = school
        self.age = age
        self.id = id
        
    def __init__(self):
        print(f"{self.school},{self.id}")    
        
c = Student()

        
    
    
    
    