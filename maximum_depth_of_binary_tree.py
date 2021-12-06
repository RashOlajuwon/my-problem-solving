"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def helper(self, root, depth):
        cur = depth
        if root==None:
            return depth
        depth+=1
        depth = max(self.helper(root.right, depth), self.helper(root.left, depth))
        if depth>cur:
            return depth
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        a = self.helper(root, depth)
        return a
