'''
COLLISIONS

'''


def collisions(alist):
    newlist = []
    sum_list = []
    
    for num in alist:
        newlist = []
        while(num > 0):                     # separating the digits
            newlist.append(num % 10)
            num //= 10
        sum_list.append(sum(newlist) % 8)   # listing the sum and division by 8

    dic = {}
    for item in sum_list:                   #creating the dictionary
        if item in dic:
            dic[item] += 1
        else:
            dic[item] = 1
    
    return dic
