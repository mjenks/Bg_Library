# gui_windows.py
# Functions for creating all of the windows used in the GUI for the board game library.

import tkinter as tk
import pandas as pd
import bg_library_funcs as bg
import button_funcs as btn

#Creates a window displaying an under devolopment message.
def Under_dev():
    window_dev = tk.Tk()
    window_dev.title("Sorry")
    msg = tk.Label(window_dev, text="Feature still in development.")
    msg.pack()
    window_dev.mainloop()

#Home display window
def Home():
    window_home = tk.Tk()

    #Make a frame for the title
    header = tk.Frame(master=window_home)
    header.pack(fill=tk.BOTH)

    #Make a frame to hold the features
    body = tk.Frame(master=window_home)
    body.pack(fill=tk.BOTH)

    #Make a grid of frames in the body that will hold buttons for features
    update = tk.Frame(master=body)
    mk_list = tk.Frame(master=body)
    random = tk.Frame(master=body)
    export = tk.Frame(master=body)

    update.grid(row=0, column=0)
    mk_list.grid(row=0, column=1)
    random.grid(row=1, column=0)
    export.grid(row=1, column=1)

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
    btn_choose = tk.Button(master=random, text="What should I play?", command=btn.random)
    btn_choose.pack()
    btn_adv = tk.Button(master=random, text="Advanced", command=btn.adv_random)
    btn_adv.pack()

    #Put a button to export library to csv file in export frame
    btn_export = tk.Button(master=export, text="Export Library to csv", command=btn.export)
    btn_export.pack()

    window_home.mainloop()



