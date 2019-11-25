#!/usr/local/bin/python3
import sys
print(sys.version)

# asa deschizi un fisier din folderul python - r,w,a(append) - append poti doar sa adaugit nu sa stergi, r+ poti sa citesti si sa stergi
employee_file = open("/Users/andrei.teodoroiu@ro.ibm.com/github/ierdna/Edu/employees.txt", "r")
print(employee_file.read())


employee_file.close()

print("__________________________________")

#asa citesti doar o linie
employee_file = open("/Users/andrei.teodoroiu@ro.ibm.com/github/ierdna/Edu/employees.txt", "r")
print(employee_file.readline())
print(employee_file.readline())

employee_file.close()


print("__________________________________")

#asa citesti tot fisierul ca o lista
employee_file = open("/Users/andrei.teodoroiu@ro.ibm.com/github/ierdna/Edu/employees.txt", "r")
print(employee_file.readlines())

employee_file.close()

print("__________________________________")

#asa citesti tot fisierul ca o lista si printezi doar ce e la index x
employee_file = open("/Users/andrei.teodoroiu@ro.ibm.com/github/ierdna/Edu/employees.txt", "r")
print(employee_file.readlines()[3])

employee_file.close()
