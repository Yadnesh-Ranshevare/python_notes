#LIST:- built in data type that store the set of value ( similar to array )

marks = [ 94.5 , 87.5 , 86.5 , 66.1 , 74.6 , 78.5 , 84.5 ]
print(marks)
print(type(marks))
print(marks[5])     # print the vale of 5th index
print(len(marks))   # print the length of list


# can store the different data type in same list and is mutable
student = ["yadnesh", 8.03 ,19 ,"kalyan"]
print(student)
print(student[1]) # print the vale of 1st index
student[2] = 20     #this is allow in list
print(student)



# list slicing
marks = [ 94.5 , 87.5 , 86.5 , 66.1 , 74.6 , 78.5 , 84.5 ]
print(marks[2:5])     # print the values from 2nd index to 5th index
print(marks[:5])      # print the values from 0th index to 5th index
print(marks[2:])      # print the values from 2nd index to end
print(marks[-3:])     # print the values from 3rd last index to end


# list method
marks = [ 94.5 , 87.5 , 86.5 , 66.1 , 74.6 , 78.5 , 84.5 ]
marks.append(85.3)          #add one element at the end
marks.insert(1,71.8)        #insert 71.8 at 1st index
print(marks)
print(marks.sort())         #it return the none
marks.sort()                #sort the list in acceding order and change the original list
print(marks)
marks.sort(reverse=True)    #sort the list in descending order 
print(marks)
marks.reverse()             #revers the list
print(marks)
letters = ['a','s','t','g','e','r','w','c']
letters.sort()              #sort the list in alphabetically ascending order
print(letters)
letters.remove('t')         #remove the first occurrence of element
print(letters)
letters.pop(3)              #remove the element at 3rd index
print(letters)
letters.pop()               #remove the last element
print(letters)
copyList = letters.copy()   #copy the letter list
print(copyList)



# TUPLE:- it is a inbuilt data type that let us create immutable sequence of value 
tup = (5 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15)
print(tup)
print(type(tup))
print(tup[5])
# tup[5] = 1                      #now allow as tuple is immutable
print(tup[1:5])                   #slicing is same as list
 
tup = (6)                         #this tuple will be of type int
print(type(tup))
singleValueTuple = (6,)           #syntax for single value tuple
print(type(singleValueTuple))


#tuple meted

tup = (5, 8, 9, 10, 11, 12, 13, 14, 15 , 9)
print(len(tup))                     #print the length of the tuple
print(max(tup))                     #print the maximum value
print(min(tup))                     #print the minimum value
print(sum(tup))                     #print the sum of the
print(tup.index(9))                 #return the index of the 1st occurrence of the element
print(tup.count(9))                 #print the number of occurrences of the element
