"""
Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.
"""

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        ans = []
        def find(root, target):
            if root==None:
                return
            if root.val == target.val:
                ans.append(root)
                return
            find(root.left, target)
            find(root.right, target)
            return
        find(cloned, target)
        return ans[0]
