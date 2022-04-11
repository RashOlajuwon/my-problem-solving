"""
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.
"""
def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid) # m rows
        n = len(grid[0]) #n cols
        allE = []
        for i in range(m):
            for j in range(len(grid[i])):
                allE.append(grid[i][j])
        i = 0
        k = k%(m*n)
        while i<k:
            a = allE.pop()
            allE.insert(0,a)
            i+=1
        print(allE)
        ans = []
        a = 0
        for i in range(m):
            b = []
            for j in range(n):
                b.append(allE[a])
                a+=1
            ans.append(b)
        return ans
