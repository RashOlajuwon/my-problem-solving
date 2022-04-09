"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        # print(d)
        res = sorted(d.keys(), key=lambda x:d[x],reverse=True)
        # print(res)
        return res[:k]
