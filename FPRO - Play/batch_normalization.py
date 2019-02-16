'''
MEDIAN BATCH NORMALIZATION
'''


def batch_norm(alist, batch_size):
    
    # creating batches
    batches = []
    for i in alist:
        if alist == []:
            break
        temp = []
        for j in range(batch_size):
            if j >= len(alist):
                break
            temp.append(alist[j])
        batches.append(temp)
        alist = alist[batch_size:]
    
    # calculating median    
    med = []
    for batch in batches:
        batch = sorted(batch)
        if len(batch) % 2 == 0:
            med.append((batch[len(batch)//2]+batch[len(batch)//2-1])/2)
        else:
            med.append((batch[len(batch)//2]))
    
    # generator
    for j in batches:
        yield list(map(lambda x: x-med[0], j))
        del med[0]
    
print(list(batch_norm([10, 1, -12, 5, 1, 3, 7, 3, 3], 5)))