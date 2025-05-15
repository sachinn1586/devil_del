print("hello World")

a = 10
b = 20
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print ("remainder of a ",a%b)


print(type(a // b))
print("the avg of the a and b is ", (a + b) / 2)
c=5
print( "the value of c is ",c**2)


#String
Name = "Sachin Kumar"
print("the name is ", Name[0:4]) 

number = "1234567890"
print("the number is ", number[0:9:2])
print(len(number))


car = "Sachin_Kumar\n not a goood boy"
print(car)


Enter = input("Enter the name of the car ")
print(f"the name of the car is {Enter} ")

default ='''Day <name>,
Day <time>'''
print(default.replace("<name>", "Sachin Kumar").replace("<time>", "10:00 AM"))

name = "Sachin Kumar    DEFAULTER JAVAYA"
x=name.replace("    ", " GOOD")
print(x) 