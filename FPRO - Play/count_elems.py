'''
5. MORE COUNTING
This function receives a tuple and counts how many elements are in each
position.
Returns a tuple with the amount of elements in each position
'''


def count_elems(tup):
    result = ()
    for elem in tup:
        if (type(elem)).__name__ == "float" or (type(elem)).__name__ == "int":
            elem = int(elem)
            elem = str(elem)
            result += (len(elem),)
        elif (type(elem)).__name__ == "complex":
            result += (1,)
        elif (type(elem)).__name__ == "bool":
            elem = str(elem)
            result += (len(elem),)
        else:
            result += (len(elem),)
    return result
            
print(count_elems(('12',2,(3, 4), [4.0, 'str', 'str2'], 5j)))