"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

def c_s(self, n, memo={}):
        if n in memo:
            return memo[n]
        elif n==0:
            return 1
        elif n==1:
            return 1
        memo[n] = self.c_s(n-1, memo)+self.c_s(n-2, memo)
        return memo[n]
        
    def climbStairs(self, n: int) -> int:
        return self.c_s(n)
