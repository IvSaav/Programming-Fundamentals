'''
MOST FREQUENT
'''


def most_frequent(alist):
    
    dic = {}
    for i in alist:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    
    alist = dic.items()
    def sort_rule(x):
        return x[1], x[0]
    alist = sorted(alist, key = sort_rule, reverse = True)
    return alist[0][0]


print(most_frequent([-1, 2, 5, -1, 3, 3, 3, 4, 4, 2, 4, 5, -1, -1]))