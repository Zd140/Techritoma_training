#nestedloops
list_fruits = ['MANGO', 'APPLE', 'GRAPES', 'BANANA']
for fruit in list_fruits:
    for i in fruit:
        print(i, end="@")
    print()