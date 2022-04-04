"""
You are given the head of a linked list, and an integer k.
Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).
"""
def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head.next==None:
            return head
        def get_len(head):
            length = 0
            cur = head
            while cur:
                length+=1
                cur = cur.next
            return length
        l = 1
        left_node = head
        while l<k:
            left_node = left_node.next
            l+=1
        r = 1
        right_node = head
        length = get_len(head)
        while r<=(length-k):
            right_node = right_node.next
            r+=1
        # print(left_node.val, l,"---",right_node.val,r)
        right_node.val, left_node.val = left_node.val,right_node.val
        return head
