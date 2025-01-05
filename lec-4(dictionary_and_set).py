# DICTIONARY:- dictionary are use to store data value in key-value pairs, they are unordered, mutable and dont allow duplicate keys
dic = {
    "key":"value",
    "name": "Yadnesh",
    "age": 19,
    "is_student": True,
    "is_employed": False,
    "marks": [94.5, 87.5, 86.5, 66.1, 74.6, 78.5, 84.5] 
}
print(dic)
print(type(dic))
print(dic["name"])
print(dic["age"])
# print(dic["abc"])                 #throw error

dic["age"] = 20                     #can change the value
dic["surname"] = "ranshevare"       #can add a new key value pair
print(dic)


# NESTED DICTIONARY
student = {
    "name" : "yadnesh",
    "marks":{
        "maths": 94.5,
        "science": 87.5,
        "english": 86.5,
        "total": 94.5 + 87.5 + 86.5
    }
}
print(student)
print(student["marks"])
print(student["marks"]["maths"])



#DICTIONARY METHODS
dic = {
    "key":"value",
    "name": "Yadnesh",
    "age": 19,
    "is_student": True,
    "is_employed": False,
    "marks": [94.5, 87.5, 86.5, 66.1, 74.6, 78.5, 84.5]
}
print(dic.keys())       #return the collection keys
print(dic.values())     #return the collection values
print(len(dic))         #return the total no of key value pair
print(dic.items())      #return the key value pairs as a tuple
print(dic.get("name"))  #return the vale of key
print(dic.get("abc"))   #doesn't throw error and return none as 'abc' key doesn't exist
# print(dic["abc"])       #throw error
new_dic = {
    "city": "Kalyan",
    "age" : 20          #this will get overwrite in old dictionary
}
dic.update(new_dic)     #insert new dictionary into old dictionary
print(dic) 




# SET:- collection of unordered items with, each element in set must be unique and immutable

set = {1 , 5 , 8 , 9 ,9 ,9 , 10 , 11 , "abc" , "efg"}       #will ignore the duplicate value
print(set)
print(type(set))

collection = {}         #empty dictionary
print(type(collection)) #it will be dictionary
collection = set()      #syntax for empty set
print(type(collection))


# SET METHOD

set = {1 , 5 , 8 , 9  , 10 , 11 , "abc" , "efg"}
set.add(55)             #add the value in set
print(set)
set.remove("abc")       #remove the value
print(set)
value = set.pop()       #pop out the random value
print(value)
print(set)
newSet = {1, 8, 9, 45, 89, "jkl"}
print(set.union(newSet))        #cobain both the sets
print(set.intersection(newSet)) #return the common values between two sets
set.clear()             #clear the set
print(set)
