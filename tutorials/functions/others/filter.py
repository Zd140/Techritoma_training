def fil(a):
    if a > 5:
        return a
    
    
out = filter((fil), (1,4,77,3,9))

print(list(out))

out = filter(lambda a:(a > 5), (1,4,7,3,9),  )

print(list(out))