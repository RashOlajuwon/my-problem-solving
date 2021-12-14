"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findDepth(self, root, depth):
        cur = depth
        if root==None:
            return depth
        depth+=1
        depth = max(self.findDepth(root.right, depth), self.findDepth(root.left, depth))
        return depth
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        depth = 0
        if root==None:
            return True
        a = self.findDepth(root.right, depth)-self.findDepth(root.left, depth)
        if abs(a)>1:
            return False
        if self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False
        
        
            
        
