class HomeSepians:
    def speak(self):
        print("Hello Sapian Speaking")
class Man(HomeSepians):
        def walk(self):
            print("Man walking")
class ManChild(Man):
        def eat(self):
            print("Eating food")
d = ManChild()
d.speak()
d.walk()
d.eat()