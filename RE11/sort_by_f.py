'''
SORT BY FUNCTION
'''

def sort_by_f(l):
    return sorted(l, key = lambda x: (5-x) if x >= 5 else x)


print(sort_by_f([-1, -2, 2, 15, 99]))