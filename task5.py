from main import get_dataframe


def exchange_columns(dataframe, col1, col2):
    col_list = list(dataframe.columns)
    x, y = col_list.index(col1), col_list.index(col2)
    col_list[y], col_list[x] = col_list[x], col_list[y]
    dataframe = dataframe[col_list]
    return dataframe


df = get_dataframe()
print('Before:')
print(df)
df = exchange_columns(df, 'Survived', 'Age')
print('After:')
print(df)


print('With sorted column names:')
print(df.sort_index(axis=1))
