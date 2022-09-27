cars = ["Jaguar","land rover",'tesla',"toyota","TATA"]
new_cars = [x if x != 'tesla' else 'audi' for x in cars]
print(new_cars)