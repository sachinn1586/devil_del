## showing the higer precedence of object attribute.
class a:
    name = "Sachin Kumar"
    age = 21
    
    
    def show(self):
        return f"the name of the value is {self.name} \n The age is {self.age}"
    
    
c = a()
c.age = 23
print(c.show())
    
#self used to refer the instance of object in a function
class apple:
    name = "sachin kumar"
    age = 21
    year = 2000
    
    def show_value(self):
        return f"the name is {self.name} age is {self.age}"
    
    def greet(n):
        print("greet")
        
d = apple()
print(d.show_value())


# static method which does not any arguments of object
# Does NOT use self (instance) or cls (class)

# Does NOT access or change object or class data
class Student:
    
    @staticmethod
    def static(name):
        print(f"the value of the number are NOM  {name}")
        
    
c = Student()
c.static("kila")


#__init__ is a special method in Python used to initialize an object when it's created. It's called automatically when you create an instance of a class.
class init:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

c =  init("qwerty",1,1001)
print(c.a,c.b,c.c)

# class Person:
#     pass

# p1 = Person()
# # You’d have to manually set values like:
# p1.name = "Bob"
# p1.age = 25


#classmethod - - You want to access or modify class-level data.
class Number:
    a =132
    @classmethod
    def clas(clse):
        print(clse.a)
        
w=Number()
a = 12
w.clas()
    















