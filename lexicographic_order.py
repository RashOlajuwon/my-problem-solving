"""
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.
"""

def removeDuplicateLetters(self, s: str) -> str:
        if len(s)==1:
            return s
        fut = {}
        for i in range(len(s)-1,-1,-1):
            if s[i] not in fut:
                fut[s[i]]=i
        stack = [s[0]]
        for i in range(1,len(s)):
            if s[i] in stack:
                continue
            while (stack and stack[-1] > s[i] and fut[stack[-1]] > i-1):
                stack.pop()

            stack.append(s[i])
        curS = ""
        for i in stack:
            curS+=i
        return curS
