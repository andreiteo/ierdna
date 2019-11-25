#!/usr/local/bin/python3
import sys
print(sys.version)

print(2**3)

def putere(numar_baza, puterea):
    result = 1
    for index in range(puterea):
        result = result * numar_baza
    return result


print(putere(3, 270))            
