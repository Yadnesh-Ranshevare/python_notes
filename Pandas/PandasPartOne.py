import pandas as pb

# # reading the external files
# df_csv = pb.read_csv('./Dataset/sales_data_sample.csv', encoding='latin1')

# df_json = pb.read_json('./Dataset/sample_Data.json')

# print(df_csv)
# print(df_json.head())


# # saving the data frame
# data = {
#     "Name":["ram", 'sham', 'yash'],
#     "Age":[20, 21, 22],
#     "City":["kalyan", 'pune', 'mumbai']
# }

# df = pb.DataFrame(data)
# print(df)

# df.to_csv('./Dataset/new_data.csv', index=False)






data = {
    "Name":["ram", 'sham', 'yash'],
    "Age":[20, 21, 22],
    "City":["kalyan", None, 'mumbai']
}

df = pb.DataFrame(data)
print(df.info())





