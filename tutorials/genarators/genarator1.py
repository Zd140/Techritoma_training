def my_gen():
    n = 1
    print('this is printed first')
    yield n
    
    n +=1
    print('this is printedsecond')
    yield n
    
    n += 1
    print('this is printed at last')
    yield n
    

for item in my_gen():
    print(item)

    