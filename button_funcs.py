# button_funcs.py
# The functions for each button option in the GUI of board game library

import tkinter as tk
import pandas as pd
import bg_library_funcs as bg
import gui_windows as gui
from tkinter import filedialog as fd
from tkinter import messagebox as msgbx
import config

#Button function for features that are not yet implimented
#Displays the under development window
def under_dev():
    msgbx.showinfo(message='This feature is still in development', title='Sorry')

#Asks for csv file name/location and updates the library
def update_csv():
    csv_filename = fd.askopenfilename()
    config.library = bg.update_database(csv_filename, config.library)

#Allows user to enter information on new or updated game(s) and then updates the library
def update_entry():
    under_dev()

#Allows user to generate lists of Titles from the library and display or save to a file
def mk_list():
    under_dev()

#Selects and displays a random Title from the library
def random(data):
    game = bg.random_choice(data)
    msgbx.showinfo(message=game[0])

#Opens a display to allow for options to filter the library before running random
def adv_random():
    under_dev()

#Ask for csv file destination/name and saves the current library there
def export():
    exportfile = fd.asksaveasfilename()
    config.library.to_csv(exportfile, index=False)


