import pandas as pb


# # adding columns
# data = {
#     "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
#     "Age":[20, 21, 22, 25, 26, 23],
#     "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
#     "salary":[10000, 20000, 30000, 40000, 50000, 60000]
# }

# df = pb.DataFrame(data)

# # direct assignment
# df["future_salary"] = df['salary'] + df['salary'] * 0.1
# print(df)

# # Insert method
# df.insert(1, "score", df['salary'] * 0.5)       
# print(df)


# # data updating
# data = {
#     "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
#     "Age":[20, 21, 22, 25, 26, 23],
#     "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
#     "salary":[10000, 20000, 30000, 40000, 50000, 60000]
# }

# df = pb.DataFrame(data)

# df['salary'] = df['salary'] + df['salary'] * 0.1

# print(df)



# removing columns
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)

new_Dataset = df.drop(columns=['City', 'Age'], inplace = True)

print("new dataset\n",new_Dataset)
print("\n original dataset\n",df)
