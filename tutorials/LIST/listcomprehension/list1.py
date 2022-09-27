#square of alll numbers
num = [1,2,3,4]
sq = []
for n in num:
    sq.append(n**2)
print(sq)

#comprehension
num = [1,2,3,4]
sq = [n**2 for n in num]
print(sq)
