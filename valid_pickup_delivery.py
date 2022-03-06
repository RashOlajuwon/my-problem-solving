"""
Given n orders, each order consist in pickup and delivery services. 
Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 
Since the answer may be too large, return it modulo 10^9 + 7.
----------------------------------------------------------------------------------------------------------
Love this problem...
it is pure combinatorial/permutative problem.
when given any n number, there will be n pickups and n deliveries, making n*2 elements.
n*2 elements can be arranged any (n*2)! ways.
all such possible arrangements where a D1 appears before a P1 are exactly the same as where a P1 appears before a D1.
Thus, a D1 appears before a P1 (n*2)!/2 ways - that is half of the initial number.
as many D and P pairs we have, as many times we must divide by 2.
Thus, if given n pairs of P and D, we will dive (n*2)! by 2**n ways.

Because the answer will be too large and may overflow, the ans was required to be returned in modulus of 10^9 + 7
"""
def factorial(self,n):
        if n-1>0:
            return n*factorial(n-1)
        else:
            return 1
def countOrders(self, n: int) -> int:
        modulo = 1000000007
        print(self.factorial(n*2))
        ans = ((self.factorial(n*2))//2**n)%modulo
        return int(ans)
