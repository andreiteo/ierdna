#!/usr/local/bin/python3
import sys
print(sys.version)

#a function is a piece of code which you are calling when you need it to do some thing
#cu def creezi o functie
#codul din functie trebuie sa fie indentat
def andrei():
    print("ma incalzesc!")

def say_hi():
    print("Hello mothafakaaa!")

#exemplu de functie care asteapta si input
def say_hi_you(name):
    print("Hello " + name + "!")

#calling the function
say_hi()
andrei()
say_hi_you(input("Zi cum te cheama: "))
