"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
"""

def helpFind(self, target, arr):
    for i in arr:
        if i==target:
            return True
    return False

def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    n = len(matrix)
    if n==1:
        return True if target in matrix[0] else False
    hi = n-1
    lo = 0
    while lo<=hi:
        mid = (hi+lo)//2
        if self.helpFind(target, matrix[mid]):
            return True
        if matrix[mid][0]<target<matrix[mid][-1]:
            return False
        if matrix[mid][-1]<target:
            lo = mid+1
        else:
            hi = mid-1
    return False
