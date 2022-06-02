"""
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
"""

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix [0])
        items=[]
        for i in range(rows):
            for j in range(cols):
                items.append(matrix[i][j])
        res = [[0 for i in range(rows)] for j in range(cols)]
        print(res)
        idx=0
        for i in range(len(res[0])):
            for j in range(len(res)):
                res[j][i] = items[idx]
                idx+=1
        return res 
