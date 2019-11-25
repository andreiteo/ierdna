#!/usr/local/bin/python3
import sys
print(sys.version)

is_male = False
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both!")
else:
    print("You are neither male nor tall!")

#aici ambele conditii trebuie sa fie indeplinite
if is_male and is_tall:
    print("You are a male or tall or both!")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not male but you are tall")
else:
    print("You are neither male nor tall!")
