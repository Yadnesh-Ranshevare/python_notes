#output statement
print("hello world!")
print("hello","im yadndesh")



#variable
name = "Yadndesh"
age = 28
is_student = True
is_employed = False
print(name,age,is_student,is_employed)



#data types
name = "Yadndesh"
age = 28
is_student = True
is_employed = False
price = 10.12
none = None     #value is not specified
print("name:",type(name))
print("age:",type(age))
print("is_student:",type(is_student))
print("is_employed:",type(is_employed))
print("price:",type(price))
print("none:",type(none))



#arithmetic operators
a=2
b=3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)



#relational_operators
a=50
b=20
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)



#assignment operator(/=, *=, %=, +=, -=)
a=10
a**=2   # power of 2
print(a)



# logical operators
a=True
b=False
print(a and b)
print(a or b)
print(not a,not b)



#type conversion 
a=2
b=4.25
sum = a + b         #python automatically convert int into float covert less superior value into superior value 
print("Sum:",sum)   #sum = 2.0 + 4.25 = 6.25



# type casting
a=2
b="3"
print(int(b)+a)     #explicitly converting the string into int



# input statement
name = input("enter your name:")
print("hello",name)