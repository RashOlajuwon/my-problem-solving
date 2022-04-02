"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
"""

if s == s[::-1]:
            return True
        
        lo, ri =0, len(s)-1
        while lo<=ri:
            if s[lo]!=s[ri]:
                temp2 = s[:ri] + s[ri+1:]
                temp = s[:lo] + s[lo+1:]
                
                return temp == temp[::-1] or temp2 == temp2[::-1]
            
            lo +=1
            ri -=1
