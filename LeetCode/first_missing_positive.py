#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        if not A: return 1
        la = len(A)

        i = 0
        while i < la:
            if i + 1 == A[i]: 
                i += 1
                continue
            if A[i] <= 0: 
                i += 1
                continue

            j = A[i]
            while j > 0 and j <= la and j != A[j-1] and j != i:
                t = A[j-1]
                A[j-1] = j
                j = t
            if j > 0 and j <= la and j != A[j-1]: A[j-1] = j

            i += 1
        
        i = 1
        while i <= la:
            if A[i-1] != i: return i
            i += 1
        return A[la-1] + 1

if __name__ == '__main__':
    s = Solution()
    assert 3 == s.firstMissingPositive([1,2,0])
    assert 2 == s.firstMissingPositive([3,4,-1,1])
    assert 2 == s.firstMissingPositive([1,1])
    assert 3 == s.firstMissingPositive([1,1,2,2])
    assert 2 == s.firstMissingPositive([1,1,3,3])
    assert 1 == s.firstMissingPositive([])
    assert 1 == s.firstMissingPositive([2])
    assert 3 == s.firstMissingPositive([2,1])
