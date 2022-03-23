"""
There is a broken calculator that has the integer startValue on its display initially. In one operation, you can:

multiply the number on display by 2, or
subtract 1 from the number on display.
Given two integers startValue and target, return the minimum number of operations needed to display target on the calculator.
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
