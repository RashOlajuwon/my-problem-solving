"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""

def robPlan(self, nums):
        rob1, rob2 = 0,0
        for i in nums:
            temp = max(i+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return temp
    
def rob(self, nums: List[int]) -> int:
    n = len(nums)
    if n==1:
        return nums[0]
    rob1 = self.robPlan(nums[1:]) # If we start from the second house, we can rob last
    rob2 = self.robPlan(nums[0:n-1]) # If we start from the frist house, we can't rob the last 

    return max(rob1,rob2)
