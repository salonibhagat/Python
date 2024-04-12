import pandas as pd
# data = {"name" : ['abc', 'pqr', 'xyz'],
#         "age" : [25,20,30]}
# df = pd.DataFrame(data)


# print(df[['name']])
# print(df[['age']])
# row = df.loc[:1]
# print(row)
# df.insert(1, 'Name', df['name'])
# print(df)
# path = 'C:\Users\inpusbtb\OneDrive - Alfa Laval\Desktop\tech docs\Sample.csv'
file = pd.read_csv('Sample.csv', encoding='ISO-8859-1')

# Error I was facing to run above command is: UnicodeDecodeError utf-8 codec can t decode byte in position invalid start byte.
#Then I add [encoding="ISO-8859-1”] while reading the file, resolve the error.

print(file)
