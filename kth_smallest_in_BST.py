"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
"""

class Solution:
    def __init__(self):
        self.lst = []
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def insert(val,lst):
            if len(lst)==0 or val>lst[-1]:
                lst.append(val)
            elif val<lst[0]:
                lst.insert(0,val)
            else:
                for i in range(len(lst)):
                    if val>=lst[i] and val<=lst[i+1]:
                        lst.insert(i+1,val)
            return
        
        def get_lst(root):
            if root:
                get_lst(root.left)
                insert(root.val,self.lst)
                get_lst(root.right)
        get_lst(root)
        # print(self.lst)  
        return self.lst[k-1]
