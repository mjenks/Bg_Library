# gui_windows.py
# Functions for creating all of the windows used in the GUI for the board game library.

import tkinter as tk
import pandas as pd
import bg_library_funcs as bg
import button_funcs as btn
from tkinter import filedialog as fd
from tkinter import messagebox as msgbx


#Home display window
class Home(tk.Frame):
    #master.title("My Board Game Library")
    def __init__(self, master=None):
        self.master = master
        self.df = bg.bg_library()
        super().__init__(master)
        
    #Make a frame for the title
        self.header = tk.Frame(self.master)
        self.header.grid(row=0,column=0, columnspan=2)

    #Make title
        self.main_lbl = tk.Label(master=self.header, text="My Board Game Library")
        self.main_lbl.pack(fill=tk.BOTH)

    #Make frames in the body that will hold buttons for features
        self.update = tk.Frame(self.master)
        self.mk_list = tk.Frame(self.master)
        self.random = tk.Frame(self.master)
        self.export = tk.Frame(self.master)

        self.update.grid(row=1, column=0)
        self.mk_list.grid(row=1, column=1)
        self.random.grid(row=2, column=0)
        self.export.grid(row=2, column=1)
        
        self.New_data_frame()
        self.List_commands()
        self.Randomizer_frame()
        self.Export_frame()
        
    def under_dev(self):
        msgbx.showinfo(message='This feature is still in development', title='Sorry')
            
    def update_csv(self):
        csv_filename = fd.askopenfilename()
        self.df.update_database(csv_filename)
            
    def update_entry(self):
        self.under_dev()
            
    def mk_list(self):
        self.under_dev()
            
    def random(self, data=None):
        if data == None:
            game = self.df.random_choice()
        else:
            game = self.df.random_choice(data)
        msgbx.showinfo(message=game[0])
            
    def adv_random(self):
        self.under_dev()
            
    def export(self):
        exportfile = fd.asksaveasfilename()
        self.df.to_csv(exportfile, index=False)

    #Fill in the update frame with buttons to allow updating the library
    def New_data_frame(self):
        update_lbl = tk.Label(master=self.update, text="Update My Library")
        update_lbl.pack(fill=tk.BOTH)
        self.btn_csv = tk.Button(master=self.update, text="From csv", command=self.update_csv)
        self.btn_csv.pack()
        self.btn_entry = tk.Button(master=self.update, text="Entry", command=self.update_entry)
        self.btn_entry.pack()

    #Put Button to get to list options in the mk_list frame
    def List_commands(self):
        self.btn_list = tk.Button(master=self.mk_list, text="Make a List", command=self.mk_list)
        self.btn_list.pack()

    #Place random selection and advanced selection buttons in random frame
    def Randomizer_frame(self):
        self.btn_choose = tk.Button(master=self.random, text="What should I play?", command=self.random)
        self.btn_choose.pack()
        self.btn_adv = tk.Button(master=self.random, text="Advanced", command=btn.adv_random)
        self.btn_adv.pack()

    #Put a button to export library to csv file in export frame
    def Export_frame(self):
        self.btn_export = tk.Button(master=self.export, text="Export Library to csv", command=self.export)
        self.btn_export.pack()


# Window to allow user to enter information for a new entry to the library
class New_Entry_window(tk.Toplevel):
    
    def __init__(self, master=None, df):
        self.master = master
        self.df = df
        
        super().__init__(master)
        
        self.title("New Entry")
        self.Entry_Frame()
        
    #button function for adding new entry to library
    def add_entry(self):
        #read in values from all entry fields
        
        
        #make a pandas dataframe from entries
        entry = {'Title' : title, 'Min Players': Min_player, 'Max Players': Max_player}
        new = pd.DataFrame(data=entry)
        
        #update the library
        self.df.add_game(new)
        
        
    def Entry_Frame(self):
        # Labels and Entry Windows for Library data fields
        
        #Add entry Button
        
        #Done/Quit button
        



# Window for filter selections for lists
def list_filter(master):
    window_list = tk.Toplevel(master)
    window_list.title("Make Board Game List")



#Window for advanced game randomizer
def adv_select(master):
    window_adv = tk.Toplevel(master)
    window_adv.title("Advanced Game Suggester")




