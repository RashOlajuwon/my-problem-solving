"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a = list1
        b = list2
        cur = dummy = ListNode()
        while a and b:
            if a.val<b.val:
                cur.next = a
                a, cur = a.next, a
            else:
                cur.next = b
                b, cur = b.next, b
        if a:
            cur.next = a
        elif b:
            cur.next = b
            
        return dummy.next
