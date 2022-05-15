"""
Given the root of a binary tree, return the sum of values of its deepest leaves.
"""

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        level_map = {}
        def accum_leaves(root,level):
            if root==None:
                return
            if level in level_map:
                level_map[level].append(root.val)
            else:
                level_map[level] = [root.val]
            accum_leaves(root.left,level+1)
            accum_leaves(root.right,level+1)
            
        accum_leaves(root,0)
        leaf_level = max(level_map.keys())
        return(sum(level_map[leaf_level]))
