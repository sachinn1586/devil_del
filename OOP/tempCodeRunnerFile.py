class A:
    
    a =232

    def show(cls):
        return f"the value are {cls.a}"
    
    
c=A()
c.a=1
print(c.show())

class A:
    
    a =23
    @classmethod
    def show(cls):
        return f"the value are {cls.a}"
    
    
c=A()
print(c.show())


#classmethod - - You want to access or modify class-level data.
