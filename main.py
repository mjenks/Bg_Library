# main.py
# run code for my board game libary
# reads in previously stored database if it exists 
# Starts the GUI 

import config
import pandas as pd
import tkinter as tk
import bg_library_funcs as bg
import gui_windows as gui
import button_funcs as btn
from tkinter import filedialog as fd
from tkinter import messagebox as msgbx
from tkinter import filedialog as fd


config.init()
master = tk.Tk()

# checks to see if there is an existing game library
# if not it asks if the user would like to load one from a csv file
if config.library.empty:
    imp = msgbx.askyesno(message='Would you like to import a csv file with your game library?', icon='question', title='Import')
    if imp:
        fname = fd.askopenfilename()
        config.library = pd.read_csv(fname)
    else:
        #msgbx.showerror(message='CSV file needed to run')
        gui.add_entry(master)
else:
    msgbx.showinfo(message='Loading your library')

gui.Home(master)


master.mainloop()


