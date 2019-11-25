#!/usr/local/bin/python3
import sys
print(sys.version)

# word - definition


#key si value - in stanga e cheia si in dreapta e valoarea

month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
}


#get te lasa sa specifici si o valoare default
print(month_conversions["Jan"])
print(month_conversions.get("aaa", "Not a valid key"))
