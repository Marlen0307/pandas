import pandas as pd
import matplotlib.pyplot as plt

from main import get_dataframe
series_list = []

df = get_dataframe()

# append series as index
i = 0
while i < len(df.index):
    series_list.append(i)
    i += 1
series = pd.Series(series_list)
print(df.set_index(series))