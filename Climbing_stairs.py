def climbStairs(self, n: int) -> int:
        """You are climbing a staircase. It takes n steps to reach the top.
        Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?"""
        
        # try solving a few steps manually and a pattern is observed that each step is a sum of the distinct ways it took to climb each of the last
        # two stairs
        # this is because, to get the present step, you either go 1 step from the last step, or go 2 steps from the last two steps
        # the ditinct ways it took to get to the last step, n and the distinct ways it took to get to the last two steps, m
        # n+m = distinct ways it takes to get to the present step
        d = {1:1, 2:2, 3:3}
        for i in range(4, n+1):
            d[i] = d[i-1]+d[i-2]
        return d[n]
