"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
"""

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        coll = []
        for i in range(rowIndex+1):
            if i == 0:
                coll.append([1])
            elif i==1:
                coll.append([1,1])
            elif i==2:
                coll.append([1,2,1])
            else:
                a = coll[i-1]
                coll.append([1]+[a[b]+a[b+1] for b in range(len(a)-1)]+[1])
        return coll[rowIndex]
