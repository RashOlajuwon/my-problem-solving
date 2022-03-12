"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
"""

def trib(self, n, memo={}):
        if n==0:
            memo[0] = 0
        elif n==1:
            memo[1] = 1
        elif n==2:
            memo[2] = 1
        else:
            memo[n]=self.trib(n-1, memo)+self.trib(n-2, memo)+self.trib(n-3, memo)
        print(memo)
        return memo[n]
            
    def tribonacci(self, n: int) -> int:
        return self.trib(n)
