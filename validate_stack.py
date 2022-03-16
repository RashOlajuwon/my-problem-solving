"""
Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.
"""

def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        n = len(pushed)
        i,j = 0,0
        for i in range(n):
            stack.append(pushed[i])
            while len(stack)!=0 and popped[j] == stack[-1]:
                stack.pop()
                j+=1
            i += 1
        print(stack)
        return stack == []
