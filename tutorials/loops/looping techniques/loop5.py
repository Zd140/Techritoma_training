animals = [{"name": "dog", "age": 11}, {"name": "lion", "age": 30},{"name": "elephant", "age": 63}, {"name": "leopard", "age": 18}]

for animals in filter(lambda i : i["age"]%2 == 0, animals):
    print(animals)