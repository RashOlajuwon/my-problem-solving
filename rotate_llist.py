"""
Given the head of a linked list, rotate the list to the right by k places.
"""

def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or head.next==None:
            return head
        li = []
        cur = head
        while cur:
            li.append(cur.val)
            cur = cur.next
        k = k%len(li)
        while k>0:
            last = li.pop()
            li.insert(0,last)
            k-=1
        cur = head = ListNode(li[0],None)
        for i in range(1, len(li)):
            cur.next = ListNode(li[i],None)
            cur = cur.next
        return head
