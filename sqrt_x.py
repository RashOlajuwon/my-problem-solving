"""
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        # we will have to use analytical method
        # a very efficient and easy one will be the Newton's approach
        if x==0:
            return 0
        cur = float(x)
        accuracy = 0.00001
        while abs(x-cur*cur)>accuracy:
            cur = 0.5*(cur + x/cur)
            print(cur)
        return int(cur)
            
        
