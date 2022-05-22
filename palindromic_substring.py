"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        #find odd centre and expand around it to find all possible pallindromes
        #find even centre and expand around it to find all possible pallindromes
        def expand(centre_x, centre_y, string):
            count = 0
            while centre_x>=0 and centre_y<len(string) and string[centre_x]==string[centre_y]:
                centre_x-=1
                centre_y+=1
                count+=1
            return count
        res = sum([expand(i,i,s)+expand(i,i+1,s) for i in range(len(s))])
        return res
