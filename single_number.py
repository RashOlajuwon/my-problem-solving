"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = {}
        for i in nums:
            if i not in counter:
                counter[i]=1
            else:
                counter[i]+=1
        # print(counter)
        for element in counter.keys():
            # print(element)
            if counter[element]==1:
                return element
        
