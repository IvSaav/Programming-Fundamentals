'''
COMPATIBLE MATRICES
'''


def compatible(A, B):
    
    if len(A[0]) == len(B):
        return "A and B can be multiplied"
    else:
        return AssertionError("A and B cannot be multiplied")
    
    
    
'''
def compatible(A,B):
    try:
        assert len(A[0]) == len(B)
    except AssertionError("A and B cannot be multiplied")
    return "A and B can be multiplied"
'''

print(compatible([[2,2, 3], [1,1]], [[5,5,5,5], [5,5,5,5]]))