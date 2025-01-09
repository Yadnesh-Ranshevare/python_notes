#FUNCTION

def sum( a , b ):       
    return a + b

def mul(a=0, b=0):      #you can also give default value which will get overwritten
    return a * b

def sub(a, b=0):        #can only give default value from right to left
    return a - b

# def div(a=3, b):        #this is not allowed

a = int(input("enter 1st num: "))

b = int(input("enter 2nd num: "))

print("Sum of",a,"and",b,"is",sum(a,b))

print("Multiplication of",a,"and",b,"is",mul(a,b))

print("Subtraction of",a,"and",b,"is",sub(a,b))



#RECURSION

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    

n = int(input("Enter a number: "))

print("Factorial of",n,"is",factorial(n))