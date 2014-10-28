#!/usr/bin/env python
#coding: utf-8

class Solution:
    def _permu(self, num, n):
        pre_e = None
        if n == 0: return [[]]
        
        r = []
        for i in range(n):
            if num[i] != pre_e:
                sub_r = self._permu(num[:i] + num[i+1:], n - 1)
                for e in sub_r:
                    r.append([num[i]] + e)
            pre_e = num[i]
        return r

    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        num.sort()
        return self._permu(num, len(num))

if __name__ == '__main__':
    print(Solution().permuteUnique([1,1,2]))
    print(Solution().permuteUnique([1,1,1]))
