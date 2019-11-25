#!/usr/local/bin/python3
import sys
print(sys.version)



def temperature_in_fahrenheit(Celsius):
    return (Celsius * 9 / 5) + 32

for i in (22.6, 32.5, 17.1):
    print(i, ": ", temperature_in_fahrenheit(i))

temp_celsius = int(input("ce temperatura vrei sa transformi din Celsius in Fahrenheit?"))
temp_fahren_final = temperature_in_fahrenheit(temp_celsius)
print(temp_fahren_final)
