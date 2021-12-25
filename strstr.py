"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        if not needle:
            return 0
        elif n==1 and n==m:
            return 0
        if not needle in haystack:
            return -1
        
        for i in range(n):
            if i+m>n:
                return -1
            elif haystack[i:i+m]==needle:
                return i
        
