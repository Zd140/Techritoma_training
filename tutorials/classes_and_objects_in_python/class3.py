class Student:
    id = 100
    name = 'Anderson'
    def display(self):
        print(self.id, self.name)

#creatng objects
s=Student()
print(s.display())