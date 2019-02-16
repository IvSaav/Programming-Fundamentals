'''
MAP REDUCE
'''


def map_reduce(n1, n2):
    
    from functools import reduce
    
    alist = range(n1, n2)
    odd = list(filter(lambda y: y % 2 != 0, alist))
    squared = list(map(lambda x: x**2, odd))
    return reduce(lambda x,y: x*y if x*y < 50 else x+y, squared)
    
print(map_reduce(0,10))