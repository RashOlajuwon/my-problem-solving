"""
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""

def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0,0
        for i in nums:
            temp = max(i+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
