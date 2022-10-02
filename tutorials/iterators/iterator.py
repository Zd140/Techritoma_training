iterable_value = 'Geeks'
iterable_obj = iter(iterable_value)
while True:
    try:
        item = next(iterable_obj)
        print(item)
    except StopIteration:
        break