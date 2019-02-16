'''
PATTERN HUNTING
'''


def pattern_hunting(l1, l2, p):
    
    res = []
    for i in range(len(l1)):
        if p in l1[i]:
            res.append(l2[i])
        elif p in l2[i]:
            res.append(l1[i])
    return sorted(res, reverse = True)


print(pattern_hunting(['a string', 'two strings', 'not here'], ['choose me', 'me too', 'but not me'], "string" ))        
            
        