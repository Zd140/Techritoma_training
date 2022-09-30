class Student:
    "this is a student class"
    age = 14
    def welcome(self):
        print("Hi, welcome to section B")

print(Student.age)
print(Student.welcome)
print(Student.__doc__)