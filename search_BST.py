"""
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.
"""

def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(root):
            if root == None:
                return None
            if root.val == val:
                return root
            if root.val < val:
                return search(root.right)
            if root.val > val:
                return search(root.left)
        return search(root)
