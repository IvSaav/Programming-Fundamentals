'''
MORE COUNTING
'''


def count_elems(tup):
    
    res = ()
    for i in tup:
        if isinstance(i, tuple) or isinstance(i , list) or isinstance(i, str):
            res += (len(i),)
        else:
            res += (1,)
    return res


print(count_elems((1,'234', 3, 4.0, (5j,))))