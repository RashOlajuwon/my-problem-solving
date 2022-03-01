class Solution:
    def refine(self, string):
        a = string.split(".")
        a = [int(i) for i in a]
        return a
    
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = self.refine(version1)
        v2 = self.refine(version2)
        # if v1[-1]==0:
        #     v1.pop()
        # if v2[-1]==0:
        #     v2.pop()
        while len(v1)!=0 and v1[-1]==0:
            v1.pop()
        while len(v2)!=0 and v2[-1]==0:
            v2.pop()
            
        # if v1==None:
        #     return -1
        # elif v2==None:
        #     return 1
        
        print(v1)
        print(v2)
        if len(v1)<=len(v2):
            n = len(v1)
        elif len(v1)>len(v2):
            n = len(v2) 
        print(n)
        #try:
        for i in range(n):
            if v1[i]>v2[i]:
                return 1
            elif v1[i]<v2[i]:
                return -1
        if len(v1)>len(v2):
            return 1
        elif len(v2)>len(v1):
            return -1
        else:
            return 0
