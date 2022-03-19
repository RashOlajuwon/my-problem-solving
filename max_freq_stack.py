"""
Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the FreqStack class:

FreqStack() constructs an empty frequency stack.
void push(int val) pushes an integer val onto the top of the stack.
int pop() removes and returns the most frequent element in the stack.
If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.
 
"""

class FreqStack:

    def __init__(self):
        self.stack = []
        self.counter = {}
        self.maxx = 0
        self.nI = 0
        self.nV = 0
        self.prev_nV = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val in self.counter:
            self.counter[val]+=1
        else:
            self.counter[val]=1
        self.maxx = max(self.maxx, self.counter[val])
        if self.counter[val]==self.maxx:
            self.nV = val
            self.prev_nV = self.nV
            self.nI = len(self.stack)-1
        
    def pop(self) -> int:
        self.counter[self.nV]-=1
        self.maxx = max(self.counter.values())
        # print("nth-1...",self.nI)
        a = self.stack.pop(self.nI)
        for i in range(len(self.stack)-1, -1, -1):
            if self.counter[self.stack[i]]>=self.maxx:
                self.prev_nV = self.nV
                self.nV = self.stack[i]
                self.nI = i
                # print("nth", self.nI)
                break
        # print(a)
        return a
