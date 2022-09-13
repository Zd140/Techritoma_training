<<<<<<< HEAD
#3 x 3 matrix
from unittest import result


X = [[12,7,3], [4,5,6], [7,8,9]]

#3 x 4 matrix
Y = [[5,8,1,2], [6,7,3,0], [4,5,9,1]]

result = [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*Y)] 
                                                        for X_row in X]
                                
print(f"the result is:")
for r in result:
    print(r)
=======
print('Hello word!')
#update this program to a program to do multiplication of two matrix provided by a use
>>>>>>> 658cb6d565911a5f42d55fcedf316ab420fc5744
