#!/usr/local/bin/python3


#types of data in python - strings, boolean, numbers
#pentru ce nu se incadreaza in astea de mai sus avem classes and objects ca sa ne creem datatype-ul nostru


class student:
#initialize function - asa defineste ce este un sudent in programul tau
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

#an object is an instance of a class - the class is just the template for the objects
