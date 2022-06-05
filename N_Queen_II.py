"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.
"""

class Solution:
    def totalNQueens(self, n: int) -> int:
        res = []
        cols = set()
        posDiag = set()
        negDiag = set()
        
        def backtrack (r):
            if r==n:
                res.append(1)
                return
            for c in range(n):
                if c in cols or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                cols.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                
                backtrack(r+1)  
                
                cols.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
        backtrack(0)
        return len(res)
