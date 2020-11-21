#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 11:04:51 2020

@author: mjenks
"""

import pandas as pd

libraryfile = "bg_library.csv"

def init():
    global library
    try:
        library = pd.read_csv(libraryfile)
    except:
        library = pd.DataFrame()

