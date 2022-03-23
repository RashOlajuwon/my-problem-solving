"""

"""
def brokenCalc(self, startValue: int, target: int) -> int:
        # Once target <= startValue, we only do subtract 1 to fit the target
        if target <= startValue:
            return startValue - target
        # Base Greedy Condition
        if target % 2 == 0:
            return 1 + self.brokenCalc(startValue, target // 2)
        else:
            return 1 + self.brokenCalc(startValue, target + 1)
