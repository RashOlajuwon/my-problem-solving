"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []
        for i in s:
            if i.isalnum():
                stack.append(i.lower())
        print(stack)
        # if len(stack)==1:
        #     return False
        if stack==stack[::-1]:
            return True
        else:
            return False
        
        
                
        
