#scope
#here z is local variable becouse it is present only inside the function
def funct3():
    z = 7
    print(z)
funct3()

#Here z has a global scoope becouse it can be accessed out tof the function to 
z = 7
def funct3():
    print(z)
funct3()

print(z)

#nb we can alter the value of a local variable by using the key word global