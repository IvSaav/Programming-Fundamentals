'''
ANAGRAMS
Given a list of strings, write a Python function anagrams(alist) that groups 
anagrams together and returns them in a nested list.
'''


def sort_rule(f):
    return (f[0].lower())   


def anagrams(alist):
    result = []
    idx = 0
    for item in alist:
        result.append([])
        result[idx].append(item)
        temp = []
        for item_2 in alist:
            if item != item_2:
                x = list(item.lower().replace(" ", ""))
                y = list(item_2.lower().replace(" ", ""))
                x.sort()
                y.sort()
                if x == y:
                    temp.append(item)
                    temp.append(item_2)
                    alist.remove(item_2)
        
        for elem in temp:
            if elem not in result[idx]:
                result[idx].append(elem)
        result[idx] = sorted(result[idx])
        idx += 1
        
    result = sorted(result, key = sort_rule)
    return result
 