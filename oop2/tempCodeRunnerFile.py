class Student:
    __count = 0  # static variable

    def __init__(self, name):
        self.name = name
        Student.__count += 1
        
    def get():
        print(self.__count)
        
    def set(self,__count):
            
        
s = Student("Sachin")
s.get()