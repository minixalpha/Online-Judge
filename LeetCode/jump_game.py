#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        max_reach, n = 0, len(A)
        for i in range(n):
            max_reach = max(max_reach, i + A[i])
            if max_reach >= n - 1: return True
            if i >= max_reach: return False
        return True

if __name__ == '__main__':
    s = Solution()
    assert True == s.canJump([2,3,1,1,4])
    assert False == s.canJump([3,2,1,0,4])
    assert True == s.canJump([2,0])
