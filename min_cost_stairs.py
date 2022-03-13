"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
"""

n = len(cost)
d = [0]*n
print(d)
d[0] = cost[0]
d[1] = cost[1]

for i in range(2,n):
    d[i] = min(d[i-1], d[i-2]) + cost[i]
return min(d[-1], d[n-2])
