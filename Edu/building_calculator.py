#!/usr/local/bin/python3
import sys
print(sys.version)

numar1 = float(input("Baga primul numar: "))
op = input("enter operator: ")
numar2 = float(input("Baga al doilea numar: "))

if op == "+":
    print(numar1 + numar2)
elif op == "-":
    print(numar1 - numar2)
elif op == "*":
    print(numar1 * numar2)
elif op == "/":
    print(numar1 / numar2)
else:
    print("ce caracter ai bagat ma?")
