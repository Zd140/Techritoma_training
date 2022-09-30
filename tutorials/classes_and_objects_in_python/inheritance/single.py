class HomeSepians:
    def speak(self):
        print("Hello Sapian Speaking")
class Man(HomeSepians):
        def talk(self):
            print("Man talking")
d = Man()
d.speak()
d.talk()