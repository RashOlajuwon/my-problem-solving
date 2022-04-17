"""
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.
"""
def increasingBST(self, root: TreeNode) -> TreeNode:
        def newBST(root,lst=[]):
            if root:
                newBST(root.left,lst)
                lst.append(root.val)
                newBST(root.right,lst)
                return lst
        lst = newBST(root)
        cur = head = TreeNode(lst[0])
        for i in range(1,len(lst)):
            cur.right = TreeNode(lst[i])
            cur = cur.right
        return head
            
