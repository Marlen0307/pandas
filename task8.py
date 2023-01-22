import pandas as pd

dict1 = {'A': [1, 2, 3], 'B': [4, 5, 6]}
dict2 = {'C': [7, 8, 9], 'D': [10, 11, 12]}

df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)

df1 = df1.assign(C=df2['C'])

print(df1)