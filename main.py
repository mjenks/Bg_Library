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

root = tk.Tk()
gui = gui.Home(root)


root.mainloop()


