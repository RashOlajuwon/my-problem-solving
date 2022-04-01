"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.
"""
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # recursive solution
        # ans = []
        # def preord(root):
        #     if root:
        #         ans.append(root.val)
        #         preord(root.left)
        #         preord(root.right)
        # preord(root)
        # return ans
        
        # iterative solution
        if root == None: return
        stack = []
        ans = []
        cur = root
        while len(stack) or cur !=None:
            while cur:
                ans.append(cur.val)
                if cur.right:
                    stack.append(cur.right)
                cur = cur.left
            if len(stack)>=1:
                cur = stack[-1]
                stack.pop()
        return ans
