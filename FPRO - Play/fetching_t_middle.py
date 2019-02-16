'''
FETCHING THE MIDDLE
'''


def fetch_middle(lists):
    
    res = []
    for item in lists:
        if len(item) % 2 == 0:
            res.append((item[int(len(item)/2)]+item[int(len(item)/2 - 1)])/2)
        else:
            res.append(item[int(len(item)//2)])
    return res


print(fetch_middle([[10,25,35,45],[100,-1,3,4],[-3,-5,-10,-20,-100]]))
            
