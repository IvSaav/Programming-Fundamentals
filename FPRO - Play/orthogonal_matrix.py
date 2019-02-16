'''
ORTHOGONAL MATRICES
'''


def is_orthogonal(mx):
    
    # transposed
    tp = []
    for i in range(len(mx)):
        tp_line = []
        for line in mx:
            tp_line.append(line[i])
        tp.append(tp_line)
    
    # creating result matrix
    res_mx = [[0 for row in range(len(mx))] for column in range(len(mx))]
    
    # multiplying mx*tp
    for x in range(len(mx)):
        for y in range(len(mx)):
            for z in range(len(mx)):
                res_mx[x][y] += mx[x][z]*tp[z][y]
    
    # cheking the result is the identity
    for idx in range(len(res_mx)):
        if res_mx[idx][idx] != 1:     # diagonal != 1?
            return False
    
    return True

print(is_orthogonal([[-1, 0], [0,1]]))
            
            
    