#!/usr/local/bin/python3
import sys
print(sys.version)

print("__________________________________")

#asa adaugi la finalul fisierului o lini pe care o vrei tu dar o adauga de fiecare data cand rulezi programul
'''
employee_file = open("/Users/andrei.teodoroiu@ro.ibm.com/github/ierdna/Edu/employees.txt", "a")
employee_file.write("Andrei - Human resources")

employee_file.close()
'''


print("__________________________________")

'''
#cu \n scrii pe urmatorul rand
employee_file = open("/Users/andrei.teodoroiu@ro.ibm.com/github/ierdna/Edu/employees.txt", "a")
employee_file.write("\nKelly - Customer Service")

employee_file.close()



print("__________________________________")

employee_file2 = open("/Users/andrei.teodoroiu@ro.ibm.com/github/ierdna/Edu/employees.txt", "r")

print(employee_file2.read())

employee_file2.close()
'''



#write only suprascrie fisierul cu ceea ce ai tu de adaugat
employee_file = open("/Users/andrei.teodoroiu@ro.ibm.com/github/ierdna/Edu/employees.txt", "w")
employee_file.write("\nKelly - Customer Service")

employee_file.close()



print("__________________________________")

employee_file2 = open("/Users/andrei.teodoroiu@ro.ibm.com/github/ierdna/Edu/employees.txt", "r")

print(employee_file2.read())

employee_file2.close()
