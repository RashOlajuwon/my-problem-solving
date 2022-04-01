"""
Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.
"""
#This was my initial solution, but iterative and brute force: Time Complexity ---> n^2*m
# def helpSplit(self, nums,m):
    #     if m==1: return sum(nums);
    #     cur = prev = 10**7
    #     for i in range(len(nums)-1):
    #         a = max(sum(nums[:i+1]),self.helpSplit(nums[i+1:],m-1))
    #         cur = min(prev, a)
    #         prev = cur
    #     return cur

# Memoized Dynamic Programming version below but still slow: n*m
def splitArray(self, nums: List[int], m: int) -> int:
        # return self.helpSplit(nums,m)
        d={}
        def split(i,m): # take just index and the new m times we must iterate thru
            if m==1: return sum(nums[i:])  # root node
            if (i,m) in d: return d[(i,m)] # if it was already memoized
            cur = prev = 10**7
            idx = i
            while i<=(len(nums)-m):
                res = max(sum(nums[idx:i+1]), split(i+1,m-1))
                cur = min(prev,res)
                prev = cur
                i+=1
            d[(i,m)]=cur
            return cur
        return split(0,m)

# temporarily trying to grasp the following solution: nlogm
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
