"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""

def canJump(self, nums: List[int]) -> bool:
        cur = 0
        n = len(nums)-1
        for i in range(n):
            cur = max(cur, nums[i]+i)
            if cur<i+1:
                return False
        if cur>=n:
            return True
        return False
