import pandas as pb

# reading the external files
df_csv = pb.read_csv('./Dataset/sales_data_sample.csv', encoding='latin1')

df_json = pb.read_json('./Dataset/sample_Data.json')

print(df_csv)
print(df_json.head())


# saving the data frame
data = {
    "Name":["ram", 'sham', 'yash'],
    "Age":[20, 21, 22],
    "City":["kalyan", 'pune', 'mumbai']
}

df = pb.DataFrame(data)
print(df)

df.to_csv('./Dataset/new_data.csv', index=False)





# .info() method
data = {
    "Name":["ram", 'sham', 'yash'],
    "Age":[20, 21, 22],
    "City":["kalyan", None, 'mumbai']
}

df = pb.DataFrame(data)
print(df.info())



# .describe() method
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)
print(df)




# shape and column
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)
print(f'shape: {df.shape}')
print(f'columns: {df.columns}')



# Accessing the rows and column
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)
print(df.iloc[0:4,0:3])


# filtration
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)

# high_salary = df[df["salary"] > 30000]
# print(high_salary)

filtered = df[(df["salary"] >= 30000) & (df["salary"] <= 40000)]
print(filtered)


