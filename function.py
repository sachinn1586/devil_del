def sam():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))    
    c = (a + b)/2
    print("The average of the two numbers is: ", c)
sam()
    

def greet():
    a = str(input("Enter your name: "))
    print("Hello " + a + ", welcome to the world of Python!")
    
greet()

# A as a Parameter
def greet(a, b):
    print("Hello " + a + ", welcome to the world of Python!")
    print("Hello " + b + ", welcome to the world of Python!")
    return "success function"
    
    
c =greet("Chole","bhatore")
print(c)

def goodbye(start, end="Enter the Valid name"):
    print(f"the values of start is {start}")
    print(end)
    
goodbye("hello","hi")



#RECUSRION
def factorial(n):
    if (n == 0 or n == 1 ):
        return 1
    else:
        print("n is: ", n)
        print("n-1: ", n-1)  
        return n * factorial(n-1)
    
print(factorial(5))


def greatest(a,b,c):
    if(a>b and a>c):
        print("a is greater")
    elif(b>c and b>a):
        print("b is greater")
    else:
        print("c is greater")
        
x = greatest(11,20,12)
print(x)
    

def temprature(c):
    f = (c * 9/5) + 32
    print("The temprature in farenheit is: ",f)


c = int(input("Enter the temprature in celsius: "))
temprature(c)



print("a")
print("b")
print("c", end="")
print("d")



#sum of n number
def sum(n):
    if (n == 0 or n==1):
        return 1
    else:
        return n + sum(n-1)
    
c = sum(4)
print(c)

def pattern(n):
    if(n==0):
        return 
    print("*"*  n)
    pattern(n-1)

pattern(5)

    
    
def inch_to_cm(num):
    return num * 2.54

ans=inch_to_cm(5)
print(ans)


def multiply(n):
    for i in range (1,11):
        print(f' {n} X {i} = {n*i}')
multiply(5)