"""
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""

def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        lst = []
        total = 0
        node = root
        # get total of all node vals and a list of all node values
        def get_total(root,lst):
            if root==None:
                return 0
            lst.append(root.val)
            total = root.val + get_total(root.left,lst) + get_total(root.right,lst)
            return total
        total=(get_total(root,lst))
        lst.sort()
        # remove all node vals equal to or less than each node val from the total
        def grtr(root,total,lst):
            if root==None:
                return None
            root.right = grtr(root.right,total,lst)
            root.left = grtr(root.left,total,lst)
            root.val = total-sum([i for i in lst if i<root.val])
            return root
        return grtr(root,total,lst)
