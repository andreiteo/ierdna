#!/usr/local/bin/python3
import pandas as pd
import numpy as np

df = pd.read_excel("/Users/andrei.teodoroiu@ro.ibm.com/Desktop/script_DRX/test1111_11252019195201/phone.xls", sheet_name="phone")
list1 = list(df['Directory Number 1'])

list2 = []
for i in list1:
    list2.append(int(i))
