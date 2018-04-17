"""Horizontal Flip
You are given an m x n 2D image matrix (List of Lists) where each integer represents a pixel. Flip it in-place along its horizontal axis.

Example:

Input image :
              1 1
              0 0
Modified to :
              0 0
              1 1"""

def flip_horizontal_axis(matrix):
    matrix.reverse()
    return matrix


print(flip_horizontal_axis([[1,1],[0,0]]))
print(flip_horizontal_axis([[1]]))
print(flip_horizontal_axis([[1,0,1],[1,0,1]]))
print(flip_horizontal_axis([[1,0],[1,0]]))
print(flip_horizontal_axis([[1,2,3],[4,5,6],[7,8,9]]))
