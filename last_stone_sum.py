"""
You are given an array of integers stones where stones[i] is the weight of the ith stone.
We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.
Return the smallest possible weight of the left stone. If there are no stones left, return 0.
"""

def lastStoneWeight(self, stones: List[int]) -> int:
    stones.sort()
    # print(stones)
    while len(stones)>0:
        stones.sort()
        if len(stones)==1:
            break
        elif stones[-1]==stones[-2]:
            stones.pop()
            stones.pop()
        elif stones[-1]!=stones[-2]:
            a = stones.pop()-stones[-1]
            stones[-1] = a
        # print(stones)
    if len(stones)>0:
        return stones[0]
    else:
        return 0
