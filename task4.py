from main import get_dataframe
import matplotlib.pyplot as plt


df = get_dataframe()
# get the columns of the dataframe
columns = list(df.columns.values)
print(columns)

column_suma = df.sum(numeric_only=True)
# get sum of listed values for each column in the dataframe

# create a pie chart
column_suma.plot.pie()

# add labels and title
plt.title('Pie Chart of Column Sums')

# show the plot
plt.show()

# create a bar chart
column_suma.plot.bar()

plt.title('Bar Chart of Column Sums')

# show the plot
plt.show()


# get sum of all values in the dataframe
print(df.sum(numeric_only=True).sum())
