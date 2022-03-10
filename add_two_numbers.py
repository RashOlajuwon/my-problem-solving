"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        int1 = 0
        cnt1 = 0
        cur2 = l2
        int2 = 0
        cnt2 = 0
        while cur1:
            int1 += cur1.val*(10**cnt1)
            cnt1 += 1
            cur1 = cur1.next
        print (int1)
        while cur2:
            int2 += cur2.val*(10**cnt2)
            cnt2 += 1
            cur2 = cur2.next
        print (int2)
        int3 = str(int1+int2)
        int3 = int3[::-1]
        print(int3)
        cur = head = ListNode(int3[0],None)
        for i in int3[1:]:
            cur.next = ListNode(i,None)
            cur=cur.next
        return head
