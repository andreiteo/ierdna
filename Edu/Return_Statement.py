#!/usr/local/bin/python3
import sys
print(sys.version)

#se foloseste in functii ca sa iei info de la functia respectiva
#fara return nu iti printeaza valoarea
def cube(value):
    return value*value*value


result = cube(4)
print(result)

#aici folosesc functia cu return statement cube ca sa ridic la patrat inputul userului
asteapta_rezultat = int(input("Ce numar vrei sa ridici la cub? "))

cubul_final = cube(asteapta_rezultat)
print(cubul_final)



#DUPA RETURN NU MAI POTI SA MAI PUI COD IN FUNCTIE,return trebuie sa fie ultima
#linie a functiei
