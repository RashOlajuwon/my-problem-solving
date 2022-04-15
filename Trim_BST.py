"""
Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.

Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.
"""
def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root==None:
            return None
        if root.val>=low and root.val<=high:
            root.left = self.trimBST(root.left,low,high)
            root.right = self.trimBST(root.right,low,high)
            return root
        return self.trimBST(root.left,low,high) if root.val>high else self.trimBST(root.right,low,high)
