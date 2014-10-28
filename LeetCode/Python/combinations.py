#!/usr/bin/env python
#coding: utf-8

class Solution:
    def _combine(self, nlist, k):
        ln = len(nlist)
        if k == 1: return [[t] for t in nlist]

        r = []
        for i in range(0, ln - k + 1):
            e = nlist[i]
            for t in self._combine(nlist[i+1:], k-1):
                r.append([e] + t)
        return r

    # @return a list of lists of integers
    def combine(self, n, k):
        return self._combine(range(1,n+1), k)

if __name__ == '__main__':
    print(Solution().combine(4,2))

