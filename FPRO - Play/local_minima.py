'''
FIND LOCAL MINIMA
'''


def local_minima(alist, n):
    nei = (n-1) // 2
    result = []
    for i in range(1, len(alist) - 1):
        local_min = False
        for adj in range(0, nei+1): 
            if adj >= i:                # checking bounds
                nxt = alist[i + adj]
                if alist[i] < nxt:
                    local_min = True        
            elif i < alist[i - adj] and i < alist[i + adj]:  # previous - next
                local_min = True
            else:
                local_min = False
        if local_min:
            result.append((alist[i], i))
    return result
                

print(local_minima([10, 3, 3, 14, 5, 7, 4], 3))
        