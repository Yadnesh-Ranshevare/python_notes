def decorator(func):
    def wrapper():
        print("this is wrapper function")
        func()
        print("this is wrapper function")
    return wrapper

def non_decorator():
    print("this is non decorator function")

new_function = decorator(non_decorator)


# here new_function will be the combination of both the functions that is
# new_function():
#     print("this is wrapper function")     # from decorator function
#     print("this is non decorator function")   # from non decorator function
#     print("this is wrapper function")     # from decorator function


new_function()



# there is another syntax for doing this which will work same as above code
def decorator_fun(func):
    def wrapper():
        print("this is wrapper function")
        func()
        print("this is wrapper function")
    return wrapper

@decorator_fun
def non_decorator_fun():
    print("this is non decorator function")

non_decorator_fun()


# how to pass argument to wrapper function
def decorator_fun(func):
    def wrapper(name):  # you can accept the non_decorator_fun argument here 
        print("this is wrapper function")
        func(name)
        print("this is wrapper function")
    return wrapper

@decorator_fun
def non_decorator_fun(name):
    print("this is non decorator function",name)

non_decorator_fun("yadnesh")

# above syntax is suitable for one function accepting argument but in case of multiple functions we have to use another syntax as wrapper have to handle lots of arguments





def decorator_fun(func):
    def wrapper(*args, **kwargs):  # you can accept the non_decorator_fun argument here in *args
        print("this is wrapper function",args,kwargs)   #output: this is wrapper function ('yadnesh', 19, 'kalyan') {}
        func(*args, **kwargs)
        print("this is wrapper function")
    return wrapper

@decorator_fun  
def non_decorator_fun(person,age,address):
    print("this is non decorator function",person,age,address)

non_decorator_fun("yadnesh",19,"kalyan")




# return the sum of positive numbers only
def decorator_fun(func):
    def wrapper(*args, **kwargs):

        new_list = []
        
        for i in args[0]:
            if(i>0):
                new_list.append(i)

        return func(new_list)       # this function will give us the sum of list which we have to return
    
    return wrapper

@decorator_fun  
def non_decorator_fun(l):
    return sum(l)

l = [1,2,3,4,-5,-6,-7]

print(non_decorator_fun(l))



