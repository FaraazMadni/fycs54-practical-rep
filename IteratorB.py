def iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

for element in [34,[4,5],(4,5),{"a":4},"abcd",4.5]:
    print(element, "is iterable:", iterable(element))

#This proves that lists,tuples,keys and strings are iterable while values are not.
    #You can't perform iteration on single values like 34 and 4.5
