from main import get_dataframe

df = get_dataframe()

# calculate the mean value for column 'A'
mean_A = df['Fare'].mean()

# fill missing values in column 'A' with the mean value
df['Fare'] = df['Fare'].fillna(mean_A)

print(df)

