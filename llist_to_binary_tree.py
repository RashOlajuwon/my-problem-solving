"""
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def llist_to_list(self, head):
        a = []
        cur = head
        while cur:
            a.append(cur.val)
            cur = cur.next
        print(a)
        return a
    
    def helper(self, a):
        if len(a)==0:
            return None
        else:
            mid = len(a)//2
            return TreeNode(a[mid], self.helper(a[0:mid]), self.helper(a[mid+1:len(a)]))
    
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        a = self.llist_to_list(head)
        return self.helper(a)
        
