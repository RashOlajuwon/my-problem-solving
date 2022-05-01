"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
"""
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_arr = []
        t_arr = []
        for i in s:
            if i=="#":
                if len(s_arr)==0: continue
                s_arr.pop(); continue
            s_arr.append(i)
        for i in t:
            if i=="#":
                if len(t_arr)==0: continue
                t_arr.pop(); continue
            t_arr.append(i)
        print(s_arr,t_arr)
        return s_arr==t_arr
