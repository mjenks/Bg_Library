# bg_library_function.py
# store all functions that can be used with boardgame library

import pandas as pd


# reads in csv file and creates or updates the main data frame
def update_database(fname,df='None'):
    new = pd.read_csv(fname)
    if df='None':
        df = new
    else:
        df = df.append(new).drop_duplicates(subset=['Title'], keep='last')

# returns a Series of Titles that meet given criteria
def list_titles(df, cond):
    list = df.loc[cond, 'Title']
    return pd.Series(list['Title'].values)

# returns a random Title from given series or dataframe
def random_choice(data)
    if isinstance(data, pd.DataFrame):
        titles = pd.Series(data['Title'].values)
    else:
        titles = data
    rand = titles.sample()
    return rand[1]

