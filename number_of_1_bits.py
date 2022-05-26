"""
Count how many 1 bits are in an unsigned integer
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        s = str(bin(n))
        # print (s)
        cnt= 0
        for i in s:
            if i=="1":
                cnt+=1
        return cnt
