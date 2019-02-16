'''
MATRIX MULTIPLICATION
This function computes the matrix multiplication between two matrices M and N
'''


def mult(M, N):
    # Checking if the multiplication is possible
    if len(M[0]) != len(N):
        return []
    # Creating the result matrix
    res_matrix = [[0 for row in range(len(N[0]))] for col in range(len(M))]
    for i in range(len(M)):
        for j in range(len(N[0])):
            for i2 in range(len(M[0])):
                res_matrix[i][j] += M[i][i2] * N[i2][j]
    return res_matrix

