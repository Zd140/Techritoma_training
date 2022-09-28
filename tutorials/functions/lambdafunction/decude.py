from functools import reduce

num = [10,40,50,60,70,30]
sum = reduce((lambda x, y:x+y), num)
print(sum)