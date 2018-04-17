"""Find the Transpose of a Square Matrix
You are given a square 2D image matrix (List of Lists) where each integer represents a pixel.
Write a method transpose_matrix to transform the matrix into its Transpose - in-place.
The transpose of a matrix is a matrix which is formed by turning all the rows of the source matrix
into columns and vice-versa.

Example:
Input image :
1 0
1 0
Modified to:
1 1
0 0
"""

# v1: standard in-place matrix transpose
def transpose_matrix(matrix):
    for i in range(len(matrix) - 1):
        for j in range(i + 1, len(matrix[i])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix

# v2: elegant zip solution
def transpose_matrix(matrix):
    matrix[:] = map(list, zip(*matrix))
    return matrix

# v3
def transpose_matrix(matrix):
    a = []
    for i in zip(*matrix):
        a.append(list(i))
    matrix[:] = a
    return matrix



print(transpose_matrix([[1,2,3],
                        [4,5,6],
                        [7,8,9]]))