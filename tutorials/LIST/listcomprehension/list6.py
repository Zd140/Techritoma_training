numbers = []
for x in range(0, 20):
  numbers.append(x%2==0)
print(numbers)

numbers = [x%2==0 for x in range(0,21)]
print(numbers)
