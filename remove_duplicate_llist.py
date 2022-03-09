"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
"""

def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        d = {}
        trash = {}
        cur = head
        i = 0
        while cur and cur.next:
            d[i] = cur.val
            if cur.next.val in d.values():
                trash[i]=cur.next.val
                b = cur.next.next
                cur.next = b
            cur = cur.next
            i+=1
        cur = head
        print(trash.values())
        while cur.next:
            if cur.next.val in trash.values():
                b = cur.next.next
                cur.next = b
                continue
            cur = cur.next
        if head.val in trash.values():
            return head.next
        else:
            return head
