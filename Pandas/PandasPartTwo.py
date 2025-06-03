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



# # removing columns
# data = {
#     "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
#     "Age":[20, 21, 22, 25, 26, 23],
#     "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
#     "salary":[10000, 20000, 30000, 40000, 50000, 60000]
# }

# df = pb.DataFrame(data)

# new_Dataset = df.drop(columns=['City', 'Age'], inplace = True)

# print("new dataset\n",new_Dataset)
# print("\n original dataset\n",df)




# # detecting missing  data
# data = {
#     "Name":["ram", None, 'yash', 'rohan', 'aditi', 'rohit'],
#     "Age":[20, None, 22, 25, 26, 23],
#     "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
#     "salary":[10000, None, 30000, 40000, 50000, 60000]
# }

# df = pb.DataFrame(data)

# print(df.isnull())
# print(df.isnull().sum())


# # handling missing data
# data = {
#     "Name":["ram", None, 'yash', 'rohan', 'aditi', 'rohit'],
#     "Age":[20, None, 22, 25, 26, 23],
#     "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
#     "salary":[10000, None, 30000, 40000, 50000, 60000]
# }

# df = pb.DataFrame(data)

# # df.dropna(inplace=True, axis=1)
# # df.fillna(0, inplace=True)
# df['Age'].fillna(df['Age'].mean() , inplace=True)
# df['salary'].fillna(df['salary'].mean() , inplace=True)
# print(df)



# # interpolate
# data = {
#     "Time":[1, 2, 3, 4, 5],
#     "Value":[10, None, 30, None, 50]
# }

# df = pb.DataFrame(data)

# df['Value'] = df['Value'].interpolate(method='linear')
# print(df)



data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 32, 25, 19, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)

df.sort_values(by=['Age','salary'], inplace=True, ascending=[False, True])
print(df)