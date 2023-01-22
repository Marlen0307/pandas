from main import get_dataframe

df = get_dataframe()

# calculate the cutoff values
upper = df['PassengerId'].quantile(0.95)
lower = df['PassengerId'].quantile(0.05)

# select only the rows within the bounds
df = df[(df['PassengerId'] < upper) & (df['PassengerId'] > lower)]

print(df)