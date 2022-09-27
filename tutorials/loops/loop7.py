#multiplaying a list
list1 = [2,4,6]
list2 = [2,4,6]
for i in list1:
    for j in list2:
        if i == j:
            continue
        print(i, '*', j, '=', i*j)