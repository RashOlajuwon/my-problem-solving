"""
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.
"""
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.lst = []
        self.pointer = -1
        def inorder(root):
            if root:
                inorder(root.left)
                self.lst.append(root)
                inorder(root.right)
        inorder(self.root)

    def next(self) -> int:
        self.pointer+=1
        return self.lst[self.pointer].val

    def hasNext(self) -> bool:
        try:
            if self.lst[self.pointer+1]: return True
        except:
            return False        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
