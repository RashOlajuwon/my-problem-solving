"""
The numeric value of a lowercase character is defined as its position (1-indexed) in the alphabet, so the numeric value of a is 1, the numeric value of b is 2, the numeric value of c is 3, and so on.

The numeric value of a string consisting of lowercase characters is defined as the sum of its characters' numeric values. For example, the numeric value of the string "abe" is equal to 1 + 2 + 5 = 8.

You are given two integers n and k. Return the lexicographically smallest string with length equal to n and numeric value equal to k.

Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.
"""

def getSmallestString(self, n: int, k: int) -> str:
        alf = "abcdefghijklmnopqrstuvwxyz"
        alf_d = {}
        i = 1
        for x in alf:
            alf_d[x]=i
            i+=1
        # print(alf_d)
        fill = ""
        char = len(alf)-1
        for i in range(1,n+1):
            # print(char)
            while char>=0 and (k - alf_d[alf[char]]) < (n-i):
                char = char-1
            fill += alf[char]
            k = k - alf_d[alf[char]]
            # char = char-1 if (char-1) >= 0 else 0
            # print("--k--",k, char)
        return fill[::-1]
