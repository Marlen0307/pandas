from main import get_dataframe
import matplotlib.pyplot as plt


df = get_dataframe()
print(df)


# create a pie chart
df['Age'].value_counts().plot.pie()

# add labels and title
plt.xlabel('Column Age')
plt.ylabel('')
plt.title('Pie Chart of Column Age')

# show the plot
plt.show()


# create a bar chart
df['Age'].value_counts().plot.bar()

plt.xlabel('Column Age')
plt.ylabel('Frequency')
plt.title('Bar Chart of Column Age')

plt.show()


