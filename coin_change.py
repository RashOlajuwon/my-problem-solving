"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def minCombo(amount):
            if amount<0:
                return 10001
            if amount==0:
                return 0
            if amount in memo:
                return memo[amount]
            memo[amount] = min([minCombo(amount-coin)+1 for coin in coins])
            return memo[amount]
            
        return minCombo(amount)
