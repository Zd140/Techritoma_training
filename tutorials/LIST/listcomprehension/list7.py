import numpy as np
A = np.random.randint(10, size=(4,4))
print(A)
max_element = [max(i) for i in A]
print(max_element)