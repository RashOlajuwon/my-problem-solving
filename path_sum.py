"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def helper(self, root, counter, target):
        if root==None:
            return False
        if root.left==None and root.right==None:
            counter+=root.val
            if counter==target:
                return True
            else:
                return False
        counter+=root.val
        return self.helper(root.left, counter, target) or self.helper(root.right, counter, target)
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        counter = 0
        if root==None:
            return False
        return self.helper(root, counter, targetSum)
        
