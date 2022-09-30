#init function

class Student:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
s1 = Student('Harry','29/10.1992')
print(s1.name)
print(s1.dob)

#modify objects
s1.name = 'Delaney'
print(s1.name)