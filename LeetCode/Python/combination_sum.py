#!/usr/bin/env python
#coding: utf-8

class Solution:
    def _cbs(self, d, t):
        if t < 0: return []
        if not d: return []
        if d[0] == t: return [[d[0]]]

        x = self._cbs(d, t - d[0])
        y = self._cbs(d[1:], t)
        for e in x:
            y.append([d[0]] + e)
        return y

    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates = list(set(candidates))
        candidates.sort()
        return self._cbs(candidates, target)

if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2,3,6,7], 7))
    print(s.combinationSum([2,2,3,6,7], 7))
