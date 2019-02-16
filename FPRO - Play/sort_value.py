'''
SORT BY VALUE
'''


def sort_by_value(dic):
    alist = dic.items()
    return sorted(alist, key = lambda x: x[1])

print(sort_by_value({"Blue":"#0000FF", "Green":"#008000", "Black":"#000000", "White":"#FFFFFF"}))