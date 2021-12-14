"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        a = helper(root)
        return a
    
def helper(root):
    if root!=None:
        if root.left==None and root.right==None:
            return 1
        return (min(helper(root.left), helper(root.right))+1)
    else:
        return 9999
