#!/usr/bin/env python
#coding: utf-8

class Solution:
    # TimeLimit 
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if not A: return 0
        la = len(A)

        ma, j, accu = A[0], 1, A[0]
        while j < la:
            if accu < 0: accu = 0
            accu = accu + A[j]
            if accu >= ma:
                ma = accu
            j += 1
        return ma

if __name__ == '__main__':
    s = Solution()
    assert 0 == s.maxSubArray([])
    assert 1 == s.maxSubArray([1])
    assert 1 == s.maxSubArray([1,-1])
    assert 3 == s.maxSubArray([1,-1,3])
    assert 1 == s.maxSubArray([-2, 1])
    assert -1 == s.maxSubArray([-2, -1])
    assert 6 == s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    assert -1 == s.maxSubArray([-1,-1,-2,-2])
    assert 4 == s.maxSubArray([3,-2,-3,-3,1,3,0])
