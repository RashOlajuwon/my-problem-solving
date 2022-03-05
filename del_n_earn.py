def deleteAndEarn(self, nums: List[int]) -> int:
      count = Counter(nums)
      prev=curr=0
      k=None
      for i in sorted(count):
          earn = i*count[i]
          if i-1==k:
              prev, curr = curr, max(prev+earn, curr)
          else:
              prev, curr = curr, curr+earn
          k=i
      return curr
