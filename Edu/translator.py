#!/usr/local/bin/python3
import sys
print(sys.version)



def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "aeiou":
            translation = translation + "g"
        elif letter in "AEIOU":
            translation = translation + "G"
        else:
            translation = translation + letter
    return translation

print(translate(input("zi ce vrei sa traduci: ")))
