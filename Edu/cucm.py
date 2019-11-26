#!/usr/local/bin/python3

numere_cumparate = range(+498741470000, +498741470011)
numere_cumparate2 = range(+498741480000, +498741480010)
numere_folosite = [+498741470001, +498741470002, +498741470010, +498741480007]





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
    print(automatizare", Numere folosite in: ")
