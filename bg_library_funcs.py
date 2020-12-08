# bg_library_function.py
# store all functions that can be used with boardgame library

import pandas as pd

#defines library object
# a pandas dataframe with boardgame library functions
class bg_library(pd.DataFrame):
    
    def __init__(self):
        libraryfile = "bg_library.csv"
        try:
            self.df = pd.read_csv(libraryfile)
        except:
            self.df = pd.DataFrame()

# reads in csv file and creates or updates the main data frame
    def update(self, fname):
        new = pd.read_csv(fname)
        if self.df.empty:
            data = new
        else:
            data = self.df.append(new).drop_duplicates(subset=['Title'], keep='last')
        self.df = data

# returns a Series of Titles that meet given criteria
    def list_titles(self, cond):
        list = self.df.loc[cond, 'Title']
        return pd.Series(list['Title'].values)

# returns a random Title from given series or dataframe
    def random_choice(self, data=pd.Series()):
        if data.empty:
            titles = pd.Series(self.df['Title'].values)
        else:
            titles = data
        rand = titles.sample()
        return rand

