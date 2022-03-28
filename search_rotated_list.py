"""
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.
"""

def search(self, nums: List[int], target: int) -> bool:
        if len(nums)==1:
            if nums[0] == target:
                return True
            else:
                return False
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                break
            if i==len(nums)-1:
                i = 0
        num = nums[i:]+nums[0:i]
        print(num)
        hi = len(num)-1
        lo = 0
        while lo<=hi:
            mid = (lo+hi)//2
            if num[mid]==target:
                return True
            if num[mid]<target:
                lo = mid+1
            else:
                hi = mid-1
        return False
