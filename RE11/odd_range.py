'''
ODD RANGE
'''


def odd_range(start, stop, step):
    alist = range(start, stop)
    odd = list(filter(lambda x: x % 2 != 0, alist))

    i = 0
    while(i < len(odd)):
        yield odd[i]
        i += step
    
print(list(odd_range(10, 0, 1)))
        