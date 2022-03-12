"""
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

"""

def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # return a copy of the node if head is none or head.next is none
        if head==None:
            cur = None
            return cur
        # if head.next==None:
        #     cur = Node(head.val)
        #     cur.next = None
        #     cur.random = 
        #     return cur
        cur = head
        d = {}
        idx = 0
        # create dict with original node and its index
        while cur:
            d[cur] = idx
            idx += 1
            cur = cur.next
        print(d)
        # create a list with corresponding random node index
        cur = head
        li = []
        while cur:
            li.append(d[cur.random] if cur.random else None)
            cur = cur.next
        print(li)
        # create a copy of the linked list
        cur = head
        n_cur = n_head = Node(head.val, None, None)
        n_d = {0:n_head}
        idx = 1
        while cur.next:
            n_cur.next = Node(cur.next.val, None, None)
            n_d[idx] = n_cur.next
            n_cur = n_cur.next
            cur = cur.next
            idx += 1
        print(n_d)
        # modify the random nodes
        i = 0
        n_head.random = n_d[li[i]] if li[i]!=None else None
        n_cur = n_head.next
        for i in range(1, len(li)):
            n_cur.random = n_d[li[i]] if li[i]!=None else None
            n_cur = n_cur.next
        return n_head
