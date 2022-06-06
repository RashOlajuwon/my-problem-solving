"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
"""

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        stackA = []
        stackB = []
        curA = headA
        curB = headB
        while curA or curB:
            if curA:
                stackA.append(curA)
                curA = curA.next
            if curB:
                stackB.append(curB)
                curB = curB.next

        prev = None        
        while stackA and stackB:
            a = stackA.pop()
            b = stackB.pop()
            if a!=b:
                break
            prev = a
        return prev 
