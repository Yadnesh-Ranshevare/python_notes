# while loop
count = 1
while count <= 10:
    print(count * 5)
    count += 1

#BREAK
while True:
    userInput = int(input("Enter your number: "))
    if userInput == 5:
        print("click wrong number")
        break       #will terminate the loop
    else:
        print("you survived")

#CONTINUE
i = 1
while i<=10:
    if i%2 == 0:
        i += 1
        continue    #will skip the current iteration
    print(i)
    i += 1





#FOR LOOP:- used for sequential traversal 

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#normal for loop
for el in list:
    print(el)


#for loop with else
for el in list:
    print(el)
else:
    print("for loop completed")


#for else loop with break

for el in list:
    if el == 5:
        break   #else part will not execute
    print(el)
else:
    print("for loop completed")




#RANGE:- return the sequence of number starting from 0(by default) and increasing by 1(by default)
for i in range(5):      #from 0 to 4 (5 excluded)
    print(i)

for i in range(5, 10):   #from 5 to 10 (10 excluded)
    print(i)


for i in range(1, 10, 2):  #from 1 to 10 (10 excluded) with step 2
    print(i)



#PASS:- null statement that does nothing. it is used as a placeholder for future code
for i in range(5):
    pass

print("loop completed")