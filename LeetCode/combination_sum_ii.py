#!/usr/bin/env python
#coding: utf-8

class Solution:
    def _cb(self, candidates, target, start, end, curR, totalR):
        if target < 0: return

        if target == 0:
            totalR.append(curR)
            return
        
        pre = None
        while start < end:
            if pre != candidates[start]: 
                pre = candidates[start]
                self._cb(candidates, target - candidates[start],
                        start + 1, end, curR + [candidates[start]], totalR)
            start += 1

        
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        candidates.sort()
        totalR = []
        self._cb(candidates, target, 0, len(candidates), [], totalR)
        return totalR


if __name__ == '__main__':
    s = Solution()
    assert [[2,2]] == s.combinationSum2([2,2,2], 4)
    s.combinationSum2([10,1,2,7,6,1,5], 8)
