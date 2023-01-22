
from main import get_dataframe

df = get_dataframe()

# select the column of interest
column = 'Age'

# create correlation matrix for the selected column
corr_matrix = df.corr(numeric_only=True)

# print the correlation matrix
print(corr_matrix[column])
