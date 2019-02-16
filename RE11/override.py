'''
OVERRRIDE OPERATION
'''


def override(l1, l2):
    a = list(filter(lambda x: x[0] not in list(map(lambda e: e[0], l2)),l1))
    result = a + l2
    result.sort(key = lambda x: x[0])
    
    return result

    
        
print(override([('c','d'),('c','e'),('a','b'),('a', 'd')],[('a','c'),('b','d')]))