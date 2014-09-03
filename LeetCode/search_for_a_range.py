#!/usr/bin/env python
#coding: utf-8

class Solution:
    def _fstart(self, A, s, e, target):
        if s > e: return None
        m = (s + e) / 2
        if A[m] == target:
            bs = self._fstart(A, s, m-1, target)
            if bs != None: return bs
            else: return m
        elif A[m] < target:
            return self._fstart(A, m+1, e, target)
        else:
            return self._fstart(A, s, m-1, target)

    def _fend(self, A, s, e, target):
        if s > e: return None
        m = (s + e) / 2
        if A[m] == target:
            bs = self._fend(A, m+1, e, target)
            if bs != None: return bs
            else: return m
        elif A[m] < target:
            return self._fend(A, m+1, e, target)
        else:
            return self._fend(A, s, m-1, target)

    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        if A == [] or target == None: return [-1, -1]
        
        la = len(A)
        start = self._fstart(A, 0, la-1, target)
        if start == None: return [-1, -1]

        end = self._fend(A, 0, la-1, target)
        return [start, end]

if __name__ == '__main__':
    s = Solution()
    assert [-1, -1] == s.searchRange([], 1)
    assert [-1, -1] == s.searchRange([1], None)
    assert [-1, -1] == s.searchRange(range(1, 5), 0)
    assert [-1, -1] == s.searchRange(range(1, 5), 6)
    assert [3, 4] == s.searchRange([5,7,7,8,8,10], 8)
    assert [3, 3] == s.searchRange([5,7,7,8,9,10], 8)
    assert [0, 0] == s.searchRange([1], 1)
    assert [0, 1] == s.searchRange([1,1,2], 1)
    assert [1, 2] == s.searchRange([0,1,1], 1)
    assert [0, 2] == s.searchRange([0,0,0,1,2,3], 0)
