LIST1 = []

for x in range(0, 8):
    print(f'Enter the value {x}: ' )
    list2 = input()
    LIST1.append(list2)
print(LIST1)
print(type(LIST1))
LIST1.sort()
print(LIST1)