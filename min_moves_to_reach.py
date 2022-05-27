"""
You are playing a game with integers. You start with the integer 1 and you want to reach the integer target.

In one move, you can either:

Increment the current integer by one (i.e., x = x + 1).
Double the current integer (i.e., x = 2 * x).
You can use the increment operation any number of times, however, you can only use the double operation at most maxDoubles times.

Given the two integers target and maxDoubles, return the minimum number of moves needed to reach target starting with 1.
"""

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        memo = {}
        def move(cur,maxD):
            if cur>=target:
                if cur>target:
                    return 100000000
                return 0
            if (cur,maxD) in memo:
                print("reused")
                return memo[(cur,maxD)]
            if maxD<=0:
                memo[(cur,maxD)] = 1 + move(cur+1,maxD)
            else:
                memo[(cur,maxD)] = 1 + min(move(cur+1,maxD), move(cur*2,maxD-1))
            return memo[(cur,maxD)] 
        return move(1,maxDoubles)
