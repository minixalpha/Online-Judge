#!/usr/bin/env python
#coding: utf-8

class Solution:
    def _si(self, A, target, s, t):
        if s > t:
            return s

        m = (s + t) / 2
        if A[m] == target: 
            return m
        elif A[m] < target: 
            return self._si(A, target, m + 1, t)
        else:
            return self._si(A, target, s, m - 1)

    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        return self._si(A, target, 0, len(A) - 1)
        

if __name__ == '__main__':
    s = Solution()
    assert 2 == s.searchInsert([1,3,5,6], 5)
    assert 1 == s.searchInsert([1,3,5,6], 2)
    assert 4 == s.searchInsert([1,3,5,6], 7)
    assert 0 == s.searchInsert([1,3,5,6], 0)
    assert 1 == s.searchInsert([1,3], 2)
