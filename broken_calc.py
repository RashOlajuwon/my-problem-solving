"""
There is a broken calculator that has the integer startValue on its display initially. In one operation, you can:

multiply the number on display by 2, or
subtract 1 from the number on display.
Given two integers startValue and target, return the minimum number of operations needed to display target on the calculator.
"""
def brokenCalc(self, startValue: int, target: int) -> int:
        # Notice the tree. From a root node, you can only go 2x on the left or -1 on the right. e.g startValue = 5, target = 8
        #                                       5
        #                                   10      4                                      
        #                               20    9   8   3 ...and so on
        # everytime we go left, it's an even bcos of 2x....unlike right, which is either even or odd.
        # Let's backtrack.
        # so if any target number is even and > the startValue, it must have been a 2-multiple. So we can divide it by 2, count 1, and repeat the function 
        # on func(startValue, target//2). 
        # If target becomes odd along the line and > than startValue, one must have been taken from an even number.
        # So count 1 again, repeat the function on func(startValue, target+1).
        # If target becomes less than startValue, it must have only been gotten by deducting one from startValue a (startValue - target) no. of times        
        
        # Once target <= startValue, we only do subtract 1 to fit the target
        if target <= startValue:
            return startValue - target
        # Base Greedy Condition
        if target % 2 == 0:
            return 1 + self.brokenCalc(startValue, target // 2)
        else:
            return 1 + self.brokenCalc(startValue, target + 1)
