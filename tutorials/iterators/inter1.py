#itteration on liststop iteration
list = [5,25,58]
my_iter = iter(list)
print(next(my_iter))
print(next(my_iter))

print(my_iter.__next__())