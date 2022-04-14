"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
"""

def generateMatrix(self, n: int) -> List[List[int]]:
        Arr = [[0]*n for _ in range(n)]
        print(Arr)
        size = n**2
        cnt = 0
        top = 0
        left = 0
        bottom = n-1
        right = n-1
        
        
        while cnt<size: # We fill the entire 2D array until we get n*n 
            # moving right
            i = left
            while i<=right and cnt<size:
                cnt+=1
                Arr[top][i]=cnt
                i+=1
            top+=1
            # moving down
            i = top
            while i<=bottom and cnt<size:
                cnt+=1
                Arr[i][right]=cnt
                i+=1
            right-=1
            # moving left
            i = right
            while i>=left and cnt<size:
                cnt+=1
                Arr[bottom][i]=cnt
                i-=1
            bottom-=1
            # moving up
            i = bottom
            while i>=top and cnt<size:
                cnt+=1
                Arr[i][left]=cnt
                i-=1
            left+=1
            # repeat
            # print(Arr)
        return Arr
