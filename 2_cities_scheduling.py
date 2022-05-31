"""
A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

My approach>>>
I iterated thru the List costs: if 1st element in each sublist is > than the 2nd element, I append to a, else, I append to b.
if b is greater than a, I dealt with b as follows;
I created a sort function called diff to get the abs value of the diff btw 1st and 2nd element of each sublist in b.
I sort b by the value if the diff btw both of the elements in each sublist. Thus, sublists that can be compromised because their 1st and 2nd element are much closer...
are at the front in b.
I then add a+b=c
I run thru c, halfway adding up 1st elements in each sublist, and the other halfway adding up 2nd elements in each sublist.

if a was greater, I reversed the process...
"""

def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        a = []
        b = []
        n = len(costs)
        for i in costs:
            if i[0]<=i[1]:
                a.append(i)
            else:
                b.append(i)
        def diff(elem):
            return abs(elem[1]-elem[0])
        
        if len(b)>len(a):
            b.sort(key=diff)
            costs_rar = a+b
            summ = 0
            for i in range(len(costs_rar)):
                if i<=(len(costs_rar)//2)-1:
                    summ+=costs_rar[i][0]
                else:
                    summ+=costs_rar[i][1]
        else:
            a.sort(key=diff)
            costs_rar = b+a
            summ = 0
            for i in range(len(costs_rar)):
                if i<=(len(costs_rar)//2)-1:
                    summ+=costs_rar[i][1]
                else:
                    summ+=costs_rar[i][0]
