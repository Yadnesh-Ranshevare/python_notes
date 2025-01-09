#we have to open the file before reading or writing
#syntax:- open("filename(file path)","mode")
# 'r':- open for reading
# 'w':- open for write
# 'x':- create a new file and open it for writing
# 'a':- open for writing and append to the end
# 'b':- binary mode
# 't':- txt file (by default)
# '+':- open the disk file for reading and writing



#READING_FILE

f = open("lec-7_demo.txt", "r")

data = f.read()     #reading the data from the file
print(data)

data = f.read(5)    #read the data of 1st 5 characters
print(data)

line1 = f.readline()  #read the data from 1st line
print(line1)
line2 = f.readline()  #read the data from 2st line
print(line2)



#WRITING_FILE:- will create the file if doesn't exist

f = open("lec-7_demo.txt", "w")

f.write("Hello world\n")  #write data to the file will overwrite the previous file 



#APPENDING_INTO_FILE:- will create the file if doesn't exist

f = open("lec-7_demo.txt", "a")

f.write("This is a new line\n")  #write data to the file will append into previous file

f.close()           #close the file



#WITH SYNTAX
with open("lec-7_demo.txt", "r") as f:
    data = f.read()
    print(data)
    #file will automatically get closed



#DELETING THE FILE
import os

os.remove("lec-7_demo.txt")  #delete the file if exists