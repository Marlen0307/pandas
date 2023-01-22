import matplotlib.pyplot as plt

from main import get_dataframe

df = get_dataframe()

# select the column of interest
column = 'Age'

# create histogram
df[column].hist()

# add labels and title
plt.xlabel(column)
plt.ylabel('Frequency')
plt.title('Histogram of column {}'.format(column))

# show the plot
plt.show()
