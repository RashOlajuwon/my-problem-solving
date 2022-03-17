"""
Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
"""

def scoreOfParentheses(self, s: str) -> int:
        stack = []
        prev = 0
        cnt = 0
        for i in s:
            if i=="(":
                stack.append(i)
                prev+=1
                step=prev
            elif i==")":
                if step<prev:
                    cnt+=0
                elif len(stack)>1:
                    cnt+=2**(len(stack)-1)
                    step=prev-1
                else:
                    cnt+=1
                stack.pop()
                    
        
        return cnt
