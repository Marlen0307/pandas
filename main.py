import pandas as pd


def get_dataframe():
    dataframe = pd.read_csv('lib/download.csv')
    return dataframe
