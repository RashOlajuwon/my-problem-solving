"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(nums)
        # print(nums)
        prev = nums[0]
        if prev!=0:
            return 0
        for i in range(1,n):
            if nums[i]-prev > 1:
                return (prev+1)
            prev = nums[i]
        return n
