"""
Given a string s, find the length of the longest substring without repeating characters.
"""

def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = 0
        prev = []
        cur = []
        for i in s:
            if i not in cur:
                cur.append(i)
            elif i in cur:
                idx = cur.index(i)
                if len(cur)>=len(prev):
                    prev = cur
                cur = cur[idx+1:]
                cur.append(i)
            cnt = max(len(prev), len(cur))
        return cnt
