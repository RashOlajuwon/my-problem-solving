"""
You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.
Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.
"""

# def minOperations(self, nums: List[int], x: int) -> int:
#         steps = [0]
#         dp = {}
#         s = ""
#         for i in nums:
#             s += str(i)
#         def reduce(x,s):
#             if x==0:
#                 dp[(x,s)]=1
#                 return 1
#             if x<0:
#                 return 100000
#             if (x,s) in dp:
#                 return dp[(x,s)]
#             dp[(x,s)] = 1+min(reduce(x-int(s[0]),s[1:]),reduce(x-int(s[-1]),s[:-1]))
#             return dp[(x,s)]
#         a = reduce(x,s)
#         return a if a<1000 else -1

# needs good solution
