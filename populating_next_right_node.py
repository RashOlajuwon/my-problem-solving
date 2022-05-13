"""
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        d={}
        def link(root, level):
            if root==None:
                return
            if level in d:
                d[level].append(root)
                d[level][-2].next = root
            else: 
                d[level] = [root]
            link(root.left, level+1)    
            link(root.right, level+1)
        link(root, 0)
        return root
