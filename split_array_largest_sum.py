"""
Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.
"""
#This was my initial solution, but iterative and brute force
# def helpSplit(self, nums,m):
    #     if m==1: return sum(nums);
    #     cur = prev = 10**7
    #     for i in range(len(nums)-1):
    #         a = max(sum(nums[:i+1]),self.helpSplit(nums[i+1:],m-1))
    #         cur = min(prev, a)
    #         prev = cur
    #     return cur

# temporarily trying to grasp the following solution
def splitArray(self, nums: List[int], m: int) -> int:
    # return self.helpSplit(nums,m)
    def canSplit(largest):
        splitNo = 0
        cur = 0
        for n in nums:
            cur+=n
            if cur>largest:
                cur = n
                splitNo += 1
        return splitNo+1<=m

    lo, hi = max(nums), sum(nums)
    res = lo
    while lo<=hi:
        mid = (lo+hi)//2
        if canSplit(mid):
            res = mid
            hi = mid-1
        else:
            lo = mid+1
    return res
