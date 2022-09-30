class Animal:
    def __init__(self, name):
        self.name = name
        
    def greet(self):
            print("hi, my name is", self.name)

a1 = Animal('Puppy')
a1.greet()
            
