# creating class
class Student:
    name="yadnesh"
    age=28

# creating object / instance
stu = Student()
print(type(stu))
print(stu.name, stu.age)





# constructor:-  __init__()
class Student:
    collage = "TEC"         #class attribute
    name = "abc"            #this will get overwritten in the constructor
    def __init__(self, name, age):      #self refer to current instance it must be given
        self.name = name        #instance attribute
        self.age = age          #instance attribute

s = Student("yadnesh", 19)
print(s)      #this will return the address of the class instance 
print(s.name, s.age,s.collage)

 




# methods
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("name:",self.name)
        print("age:",self.age)

    @staticmethod       #decorator
    def welcome():      # static methods ( methods that won't use self parameters and works at class level )
        print("welcome to the class")

s = Student("yadnesh", 19)
s.name = "iron man"
s.display()
s.welcome()






# abstraction
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    
    def start(self):
        self.clutch = True
        self.acc = True
        print("car started")

c = Car()
c.start()   #hiding the logic of how the car is started and only showing the car started message






# encapsulation
class Car:
    def __init__(self):
        self.__acc = False      #private attribute which are not accessible from outside classes
        self.__brk = False      #private attribute which are not accessible from outside classes
        self.__clutch = False       #private attribute which are not accessible from outside classes
    
    def start(self):
        self.__clutch = True
        self.__acc = True
        print("car started")


    def __reset(self):      #private method which are not accessible from outside classes
        self.__acc = False
        self.__brk = False
        self.__clutch = False
        print("car reset")

    def stop(self):
        print("car stopped")
        self.__reset()      #can only call private method from inside the class

c = Car()

# print(c.__acc)  # this will throw error as it is private attribute
# c.__reset()     #will throw error

c.start()
c.stop()

del c   #to delete the class instance can also delete the attribute
# print(c)        #will throw error 





# single level inheritance
class Car:      #parent class
    color = "black"
    @staticmethod
    def start():
        print("car started")
    
    @staticmethod
    def stop():
        print("car stopped")

class BMW(Car):         #child class
    def __init__(self, name):
        self.name = name

car = BMW("abc")
car.start()
car.stop()
print(car.color)


# multi level inheritance
class Collage:
    clg = "TEC"
    @staticmethod
    def greeting():
        print("Welcome to our collage")

class Branch(Collage):
    branch = "IT"
    def __init__(self,year):
        self.year = year

class Student(Branch):
    def __init__(self, name, age,year):
        self.name = name
        self.age = age
        super().__init__(year)  #calling the constructor of parent class
        super().greeting()      #can also call the methods of parent class

stu = Student("yadnesh",19,2)

print(stu.name, stu.age, stu.branch, stu.clg, stu.year)


# multiple inheritance
class A:
    varA = "welcome to class A,"
class B:
    varB = "welcome to class B,"

class C(A, B):
    varC = "welcome to class C"

obj = C()

print(obj.varA,obj.varB,obj.varC)





# class method:- changing the class attributes( static methods cannot change class attributes )
class Person:
    name = "not define"
    @classmethod
    def changeClassAttribute(cls,name):
        cls.name = name

    def changeName(self,name):
        self.__class__.name = name

    def __init__(self,name):
        Person.name = name


print(Person.name)
p = Person("abcdefg")
print(Person.name)
p.changeName("yadnesh")
print(Person.name)
p.changeClassAttribute("none")
print(Person.name)






# @property:- decorator in Python is used to define a method that behaves like an attribute
class Student:
    def __init__(self,phy,chem,math ):
        self.phy = phy
        self.chem = chem
        self.math = math
    
    @property
    def total(self):
        return self.phy + self.chem + self.math

s = Student(80, 90, 75)
print("Total marks:", s.total)

s.phy = 42
print("Updated total marks:", s.total)






# polymorphism
class complex:
    def __init__(self, real, im):
        self.real = real
        self.im = im

    def ShowNum(self):
        print("Complex number is: ", self.real, "+", self.im, "i")

    def __add__(self,num2):     #dander function for addition 
        newReal = self.real + num2.real
        newImg = self.im + num2.im
        return complex(newImg,newReal)

num1 = complex(1,5)
num1.ShowNum()
num2 = complex(2,5)
num2.ShowNum()

num3 = num1 + num2      #+ sign comes because of dander function
num3.ShowNum()
