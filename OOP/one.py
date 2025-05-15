class employee:
    name="Sachin"
    age=20
    salary=20000
    
lolo = employee()
sample_ID = 12#object ka instance which is having higer preeference.
print(lolo.name,sample_ID,lolo.age,lolo.salary) 


# self is used to refer the instance of the class. It is used to access variables that belong to the class.
class explain:
    name= "Ajaa\y"
    age=121
    type="!221"
    
    
    def display(self):
        print(f"the age type is {self.type}")
        
    def greet(n):
        print("Hello")
        
        
c=explain()
c.display()
c.greet()