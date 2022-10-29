##this program prints the area of triangle
print('enter the side of the traingle: ')
a = int(input(''))
b = int(input(''))
c = int(input(''))

##calculating the half perimeter
s = (a*b*c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5

print('the area of the traingle is', area)