#Avg of possitive numbers

num = 0
count = 0
sum = 0

while num >= 0 :
    num = int(input('Enter possitive intergers: '))
    if num >=0 :
        count = count+1
        sum = sum + num
avg = sum / count
print('Total sum of numbers',  sum, 'Average: ', avg)
