#perfect number

a = 1
while a <= 100:
    y_sum = 0
    
    for i in range(1, a):
        if a%i == 0:
            y_sum= y_sum +i
        if y_sum == a:
            print("Perfect number:", a)
        a = a+1