#!/usr/local/bin/python3
import sys
print(sys.version)



#ca sa nu se opreasca din rulat si sa iti arate ca ai input gresit in loc sa iti dea eroare
'''
try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except:
    print("invalid_input")
'''





# you can except only specific lines
try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("eroare de zero")
except ValueError:
    print("eroare de valoare")



#aici printezi si eroarea
    try:
        value = 10/0
        number = int(input("Enter a number: "))
        print(number)
    except ZeroDivisionError as err:
        print("err")
    except ValueError:
        print("eroare de valoare")
