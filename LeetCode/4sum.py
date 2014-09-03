#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
     def fourSum(self, num, target):
        num.sort()
        ln = len(num)
        ans = set([])
        sum_tuple = {}
        for i in range(ln):
            for j in range(i-1):
                a = num[i-1] + num[j]
                if not a in sum_tuple: 
                    sum_tuple[a] = set([])
                sum_tuple[a].add((num[j], num[i-1]))
            
            for k in range(i+1, ln):
                b = num[i] + num[k]
                for tp in sum_tuple.get(target - b, []):
                    ans.add((tp[0], tp[1], num[i], num[k]))

        lans = []
        for a in ans:
            lans.append(list(a))
        return lans

if __name__ == '__main__':
    s = Solution()
    print(s.fourSum([1,0,-1,0,-2,2], 0))
    print (s.fourSum([ -493,-482,-482,-456,-427,-405,-392,-385,-351,-269,-259,-251,-235,-235,-202,-201,-194,-189,-187,-186,-180,-177,-175,-156,-150,-147,-140,-122,-112,-112,-105,-98,-49,-38,-35,-34,-18,20,52,53,57,76,124,126,128,132,142,147,157,180,207,227,274,296,311,334,336,337,339,349,354,363,372,378,383,413,431,471,474,481,492], 6189))
    print(s.fourSum([0,0,0,0], 0))

    print(s.fourSum([-3,-2,-1,0,0,1,2,3], 0))
