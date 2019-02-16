'''
SORT BY KEY
'''


def sort_by_key(dic):
    alist = dic.items()
    alist = sorted(alist, key = lambda x: x[0])
    return alist


print(sort_by_key({"Blue":"#0000FF", "Green":"#008000", "Black":"#000000", "White":"#FFFFFF"}))