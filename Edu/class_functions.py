#!/usr/local/bin/python3

from student import Student

student1 = Student("Oscar", "Accounting", 3.1)
student2 = Student("Philis", "Business", 3.8)

print(student1.on_honor_roll())
print("Is ", student1.name, "on the honour roll? ", student2.on_honor_roll())
