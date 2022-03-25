"""
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.
"""
def numRescueBoats(self, people: List[int], limit: int) -> int:
#         people = sorted(people)
#         lo = 0
#         hi = len(people)-1
#         boats = 0
#         while lo <= hi:
#             if people[lo] + people[hi] <= limit:
#                 lo += 1
#                 hi -= 1
#             else:
#                 hi -= 1
#             boats += 1
#         return boats 
        hi = len(people)-1
        lo = 0
        ppl = sorted(people)
        # print(ppl)
        cnt = 0
        while lo<=hi:
            if ppl[lo]+ppl[hi]<=limit:
                cnt+=1
                lo+=1
            else:
                cnt+=1
            hi-=1
        return cnt
