'''
REARRANGING
'''


def rearrange(l):
    
    neg = list(filter(lambda x : x <= 0, l))
    pos = list(filter(lambda y : y > 0, l))
    return neg + pos


print(rearrange([12, 11, -13, -5, 6, -7, 5, -3, -6, 0]))
