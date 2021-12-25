"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==1:
            return False
        elif s[0] in [')',']','}']:
            return False
        
        d = {")":"(", "]":"[", "}":"{"}
        stack = []
        for op in s:
            # print(stack)
            if op in ['(', '[', '{']:
                stack.append(op)
                # print(1)
            elif stack==[] or stack.pop() != d[op]:
                # print(2)
                return False
        if not stack==[]:
            return False
        else:
            return True
                
                
        
