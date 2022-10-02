list1 = [2,3,8,10]
list_ = [x**2 for x in list1]

genarator = (x**2 for x in list1)
print(list_)
print(genarator)
for item in genarator:
    print(item)