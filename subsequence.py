"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""

def isSubsequence(s):
        s = [i for i in s[::-1]]
        print(s)
        if not s:
            return True
        for i in range(len(t)):
            if not s:
                break
            if t[i]==s[-1]:
                s.pop()
        if s:
            return False
        else:
            return True
