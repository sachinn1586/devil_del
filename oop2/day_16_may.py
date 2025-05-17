#pass by refrence 
class person:
    def __init__(self,gender,name):
        self.name = name 
        self.gender = gender
        
def sample(person):
    print(f"Gender of the person is {person.gender}and the name is {person.name}")
    
c = person("Male","Sachin Kumar")
sample(c)
print(id(c))

#humnae pass class ko as object to a function and via-verse
#fuction is returing object of class in output

#Encapsulation - Encapsulation is the concept of hiding internal details of a class and exposing only what's necessary. This is done by making variables private (or protected) and controlling access through methods (getters/setters).


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance =self.__balance + amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance = self.__balance -  amount
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.__balance



acct = BankAccount("Alice", 1000)

acct.deposit(500)
acct.withdraw(200)

print(acct.get_balance())  # ✅ Output: 1300

print(acct.__balance)      # ❌ Error: private variable


class Student:
    def __init__(self, name):
        self.name = name
        self.__grade = 0  # private variable

    # Getter method   
    def get_grade(self):
        return self.__grade

    # Setter method
    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Invalid grade! Must be between 0 and 100.")
            
s1 = Student("John")

s1.set_grade(85)                # Valid
print(s1.get_grade())           # Output: 85

s1.set_grade(150)               # Invalid
print(s1.get_grade())           # Still 85

print(s1.__grade)               # ❌ Error: can't access private variable


#stoing the object into a list
class person:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender 

p1 = person("Sachin","M")
p2 = person("sachin2","M")
 
listt =  [p1,p2]
for i in listt:
    print(i.name,i.gender)


##Static Variable 
class Student:
    __count = 0  # static variable

    def __init__(self, name):
        self.name = name
        Student.__count += 1
        
    def get(self):
        print(self.__count)
        
    def set(self,__count):
        self.__count = __count
        
s = Student("Sachin")
s.get()        
        
        
print(Student.__count)  # 0
s1 = Student("Alice")
s2 = Student("Bob")
print(Student.__count)  # 2
