"""
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.
"""

class Solution:
    def __init__(self):
        self.lst = []
        
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def check(root):
            if root:
                check(root.left)
                self.lst.append(root)
                check(root.right)
        check(root)
        sorted_lst = sorted(self.lst, key=lambda x:x.val)
        for i in range(len(self.lst)):
            if self.lst[i].val!=sorted_lst[i].val:
                self.lst[i].val,sorted_lst[i].val = sorted_lst[i].val,self.lst[i].val
                break
