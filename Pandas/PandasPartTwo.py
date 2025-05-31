import pandas as pb


# adding columns
data = {
    "Name":["ram", 'sham', 'yash', 'rohan', 'aditi', 'rohit'],
    "Age":[20, 21, 22, 25, 26, 23],
    "City":["kalyan", None, 'mumbai', 'pune', 'nagpur', 'banglore'],
    "salary":[10000, 20000, 30000, 40000, 50000, 60000]
}

df = pb.DataFrame(data)

# # direct assignment
# df["future_salary"] = df['salary'] + df['salary'] * 0.1
# print(df)

df.insert(1, "score", df['salary'] * 0.5)       
print(df)