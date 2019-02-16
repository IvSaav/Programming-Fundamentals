'''
N-TH LOWEST
'''


def nth_lowest(lnum, n):
    
    for i in range(n-1):
        m = min(lnum)
        del lnum[lnum.index(m)]
    return min(lnum)

print(nth_lowest([73,100,23,18,84,61,56,75,92,38,54,73,3,13], 12))