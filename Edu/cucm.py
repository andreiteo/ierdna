#!/usr/local/bin/python3
import pandas as pd
import numpy as np


numere_cumparate = range(49874196471005, 49874196471010)
numere_cumparate2 = range(498741480000, 498741480010)



#aici importi numerele si pe faci int
df = pd.read_excel("/Users/andrei.teodoroiu@ro.ibm.com/Desktop/script_DRX/test1111_11252019195201/phone.xls", sheet_name="phone")
list1 = list(df['Directory Number 1'])

numere_folosite = []
for i in list1:
    numere_folosite.append(int(i))




#functia care verifica daca nr este in use sau nu
def verificare_numar(a):
    for i in a:
        if i in numere_folosite:
            print("Numarul este folosit")
        else:
            print(i)
'''
verificare_VIB = verificare_numar(numere_cumparate)
print("Numere verificate in VIB: ",verificare_VIB)

verificare_VIB2 = verificare_numar(numere_cumparate2)
print("Numere verificate in VIB2:",verificare_VIB2)
'''

lista_completa = [numere_cumparate, numere_cumparate2]
for i in lista_completa:
    automatizare = verificare_numar(i)
    print(automatizare)
