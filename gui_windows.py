# gui_windows.py
# Functions for creating all of the windows used in the GUI for the board game library.

import tkinter as tk
import pandas as pd
import bg_library_funcs as bg
import button_funcs as btn
import config


#Home display window
def Home(master):
    master.title("My Board Game Library")

    #Make a frame for the title
    header = tk.Frame(master)
    header.grid(row=0,column=0, columnspan=2)

    #Make title
    main_lbl = tk.Label(master=header, text="My Board Game Library")
    main_lbl.pack(fill=tk.BOTH)



    #Make frames in the body that will hold buttons for features
    update = tk.Frame(master)
    mk_list = tk.Frame(master)
    random = tk.Frame(master)
    export = tk.Frame(master)

    update.grid(row=1, column=0)
    mk_list.grid(row=1, column=1)
    random.grid(row=2, column=0)
    export.grid(row=2, column=1)

    #Fill in the update frame with buttons to allow updating the library
    update_lbl = tk.Label(master=update, text="Update My Library")
    update_lbl.pack(fill=tk.BOTH)
    btn_csv = tk.Button(master=update, text="From csv", command=btn.update_csv)
    btn_csv.pack()
    btn_entry = tk.Button(master=update, text="Entry", command=btn.update_entry)
    btn_entry.pack()

    #Put Button to get to list options in the mk_list frame
    btn_list = tk.Button(master=mk_list, text="Make a List", command=btn.mk_list)
    btn_list.pack()

    #Place random selection and advanced selection buttons in random frame
    btn_choose = tk.Button(master=random, text="What should I play?", command=lambda: btn.random(config.library))
    btn_choose.pack()
    btn_adv = tk.Button(master=random, text="Advanced", command=btn.adv_random)
    btn_adv.pack()

    #Put a button to export library to csv file in export frame
    btn_export = tk.Button(master=export, text="Export Library to csv", command=btn.export)
    btn_export.pack()


# Window to allow user to enter information for a new entry to the library
def add_entry(master):
    window_entry = tk.Toplevel(master)
    window_entry.title("My Board Game Library Entry")
    
    btn.under_dev()


# Window for filter selections for lists
def list_filter(master):
    window_list = tk.Toplevel(master)
    window_list.title("Make Board Game List")



#Window for advanced game randomizer
def adv_select(master):
    window_adv = tk.Toplevel(master)
    window_adv.title("Advanced Game Suggester")




