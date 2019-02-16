'''
COUNTING ELEMETS
This function receives a tuple and returns the number of elements that appear
before a tuple
If there isn´t a nested tuple it returns -1
'''


def count_until(tup):
    for i in range(0,len(tup)):
        if (type(tup[i])).__name__ == "tuple":
            return i
    return -1        
            