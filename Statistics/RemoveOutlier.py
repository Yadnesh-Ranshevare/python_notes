import pandas as pb

data = {
    "data": [10, 12, 12, 14, 13, 15, 16, 102, 19, 20, 14, 13, 17, 18, 19, 110, 17,  19, 10, 10, 11, 9, 10, 13, 100]
}

df = pb.DataFrame(data)

Q1 = df["data"].quantile(0.25)
Q3 = df["data"].quantile(0.75)
IQR = Q3 - Q1

lower_fence = Q1 - 1.5 * IQR
higher_fence = Q3 + 1.5 * IQR

outliers = []
for(index, value) in df.iterrows():
    if value["data"] < lower_fence or value["data"] > higher_fence:
        outliers.append(value["data"])

print(lower_fence)
print(higher_fence)
print(outliers)