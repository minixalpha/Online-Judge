#!/usr/bin/env python
#coding: utf-8

class Solution:
    def subsets(self, S):
        S.sort()
        return self._subsets(S) 

    def _subsets(self, S):
        if not S: return [[]]

        x = S[0]
        y = self._subsets(S[1:])
        z = []
        for i in y:
            z.append([x] + i)
        z.extend(y)
        return z

if __name__ == '__main__':
    print(Solution().subsets([3,2,1]))
