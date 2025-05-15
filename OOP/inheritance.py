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
# class A:
#     def __init__(self,name):
#         self.name = name
        
# class B(A):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age = age


# c= B("Sachin",20)
# print(c.name)
# print(c.age) 

#multiple inheritance
# Parent class 1
class ElectricVehicle:
    def charge_battery(self):
        return "Battery charging..."

# Parent class 2
class SmartCarFeatures:
    def enable_autopilot(self):
        return "Autopilot enabled."

# Child class inherits from both
class TeslaModelX(ElectricVehicle, SmartCarFeatures):
    def drive(self):
        return "Tesla Model X is now driving."

# Create object
car = TeslaModelX()

# Use methods from both parent classes and its own
print(car.drive())             # Tesla Model X is now driving.
print(car.charge_battery())    # Battery charging...
print(car.enable_autopilot())  # Autopilot enabled.


#multilevel
# Base class (Level 1)
class Vehicle:
    def general_info(self):
        return "This is a vehicle."

# Intermediate class (Level 2)
class Car(Vehicle):
    def car_info(self):
        return "This is a car, a type of vehicle."

# Derived class (Level 3)
class Tesla(Car):
    def model_info(self):
        return "This is a Tesla Model S, an electric car."

# Create object of the bottom-most class
my_car = Tesla()

# Access methods from all three levels
print(my_car.general_info())  # From Vehicle
print(my_car.car_info())      # From Car
print(my_car.model_info())    # From Tesla
