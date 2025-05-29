import pandas as pb


# read data from csv file into dataframe
df_csv = pb.read_csv('./Dataset/sales_data_sample.csv', encoding='latin1')

df_json = pb.read_json('./Dataset/sample_Data.json')

print(df_csv)
print(df_json)

