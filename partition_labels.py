"""
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
Return a list of integers representing the size of these parts.

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
"""

def partitionLabels(self, s: str) -> List[int]:
        if len(s)==1:
            return [1]
        last_appr = {}
        n = len(s)-1
        for i in range(n,-1,-1):
            if s[i] in last_appr:
                continue
            last_appr[s[i]] = i
        print(last_appr)
        fut = last_appr[s[0]] if last_appr[s[0]] != 0 else 0 
        cur = 0
        ans = []
        for i in range(n+1):
            if i==fut:
                ans.append(len(s[cur:fut+1]))
                cur = fut+1
                try:
                    fut = last_appr[s[cur]]
                except:
                    fut = cur
            if last_appr[s[i]]<=fut:
                continue
            fut = last_appr[s[i]]
        return ans
