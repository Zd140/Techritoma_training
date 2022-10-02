class Calculation:
    def sum(self, x,y):
        return x+y
class Calculation1:
    def subtration(self, x,y):
        return x-y;
class derived(Calculation,Calculation1):
    def multiplication(self, x,y):
        return x*y
d = derived()
print(d.sum(40,80))
print(d.subtration(40,80))
print(d.multiplication(20, 50))

