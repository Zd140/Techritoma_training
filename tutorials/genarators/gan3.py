def pow():
    n = 0
    yield 2 **n
    
x = pow()
print(next(x))

for item in pow():
    print(item)