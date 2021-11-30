def climbStairs(self, n: int) -> int:
        d = {1:1, 2:2, 3:3}
        for i in range(4, n+1):
            d[i] = d[i-1]+d[i-2]
        return d[n]
