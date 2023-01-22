from main import get_dataframe

dframe = get_dataframe()
dframe.loc[dframe['Survived'] == 1, 'Survived'] = True
print(dframe)
