#!/usr/local/bin/python3

numere_cumparate = int(input("Primul numar din range: "))

numere_cumparate2 = int(input("Ultimul numar din range: "))


range_ul_de_verificat = range(numere_cumparate, numere_cumparate2)
print(range_ul_de_verificat)

numere_folosite = [+498741470001, +498741470002, +498741470010, +498741480007]


for i in range_ul_de_verificat:
    if i in numere_folosite:
        print("Number used")
    else:
        print(i)








'''
verificare_VIB = verificare_numar(numere_cumparate)
print("Numere verificate in VIB: ",verificare_VIB)

verificare_VIB2 = verificare_numar(numere_cumparate2)
print("Numere verificate in VIB2:",verificare_VIB2)
'''
