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


# # sorting
# data = {
#     "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
#     "Age":[20, 21, 32, 25, 19, 23],
#     "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
#     "salary":[10000, 20000, 30000, 40000, 50000, 60000]
# }

# df = pb.DataFrame(data)

# df.sort_values(by=['Age','salary'], inplace=True, ascending=[False, True])
# print(df)



# # Aggregation function
# data = {
#     "Value":[1, 2, 3, 4, 5, 5]
# }

# df = pb.DataFrame(data)

# print(df['Value'].sum())
# print(df['Value'].mean())
# print(df['Value'].median())
# print(df['Value'].min())
# print(df['Value'].max())
# print(df['Value'].count())
# print(df['Value'].std())
# print(df['Value'].var())
# print(df['Value'].prod())
# print(df['Value'].unique())


# # Grouping in Pandas
# data = {
#     "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
#     "Age":[20, 21, 22, 21, 23, 22],
#     "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
#     "salary":[30000, 20000, 10000, 20000, 50000, 10000]
# }

# df = pb.DataFrame(data)

# grouped = df.groupby(['Age','salary'])
# for group in grouped:
#     print(group)



# # merging of data
# customers = {
#     "id":[1, 2, 3, 4, 5, 6],
#     "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit']
# }

# orders = {
#     "id":[1, 2, 3, 4, 5, 7],
#     "order_amount":[10000, 20000, 30000, 40000, 50000, 60000]
# }

# df_customers = pb.DataFrame(customers)
# df_orders = pb.DataFrame(orders)

# df_inner_merged = pb.merge(df_customers, df_orders, how='inner', on='id')
# df_outer_merged = pb.merge(df_customers, df_orders, how='outer', on='id')
# df_left_merged = pb.merge(df_customers, df_orders, how='left', on='id')
# df_right_merged = pb.merge(df_customers, df_orders, how='right', on='id')

# print("inner join\n",df_inner_merged,"\n")
# print("outer join\n",df_outer_merged,"\n")
# print("left join\n",df_left_merged,"\n")
# print("right join\n",df_right_merged,"\n")



# concatenation
list_customers_1 = {
    "id":[1, 2, 3],
    "Name":["ram", 'sham', 'yash']
}

list_customers_2 = {
    "id":[4, 5, 6],
    "Name":["rohan", 'aditi', 'rohit']
}

df_customers_1 = pb.DataFrame(list_customers_1)
df_customers_2 = pb.DataFrame(list_customers_2)

df_concat = pb.concat([df_customers_1, df_customers_2],ignore_index=True, axis=1)
print(df_concat)

# 


