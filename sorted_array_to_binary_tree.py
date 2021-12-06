"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def helper(self, nums):
        if len(nums)==0:
            return None
        else:
            a = len(nums)//2
            print(nums[a])
            return TreeNode(nums[a], self.helper(nums[0:a]), self.helper(nums[a+1:len(nums)]))

    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.helper(nums)
