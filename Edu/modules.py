#!/usr/local/bin/python3
import sys
print(sys.version)
import random

feet_in_mile = 5280
meters_in_kilometer = 1000
beatles = ["Andrei", "stefana", "Ioana"]

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(num):
    return random.randint(1, num)



rezultat = (roll_dice(int(input("cate fete are zarul? "))))

print("Ai dat: ", rezultat)
