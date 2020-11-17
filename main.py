# main.py
# run code for my board game libary
# reads in previously stored database if it exists 
# Starts the GUI 

import pandas as pd
import tkinter as tk
import bg_library_funcs as bg
import gui_windows as gui
import button_funcs as btn
from tkinter import filedialog as fd

libraryfile = bg_library.csv
try:
    library = pd.read_csv(libraryfile)
except:
    library = fd.askopenfilename()

gui.Home(library)


