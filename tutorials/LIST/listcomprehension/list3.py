cars = ["Jaguar","land rover",'tesla',"toyota","tata"]
newlist = []
for x in cars:
    if "s" in x:
        newlist.append(x)
print(newlist)

#shortform
cars = ["Jaguar","land rover",'tesla',"toyota","TATA"]
newlist = [x for x in cars if "a" in x]
print(newlist)