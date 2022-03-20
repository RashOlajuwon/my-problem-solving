"""
In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.
"""

def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        total = len(tops)
        top_fr, bot_fr, val_total = [0]*7, [0]*7, [total]*7
        print(top_fr, bot_fr, val_total, sep="\n")
        for top, bot in zip(tops, bottoms):
            if top == bot:
                val_total[top] -= 1
            else:
                top_fr[top] += 1
                bot_fr[bot] += 1
                
        for val in range(1, 7):
            if (val_total[val] - top_fr[val]) == bot_fr[val]:
                return min(top_fr[val], bot_fr[val])
            
        return -1
