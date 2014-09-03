#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        left, right = 0, len(A) - 1
        total, block = 0, 0
        curlevel = 0

        while left <= right:
            curmin = min(A[left], A[right])
            if curmin > curlevel:
                total += (curmin - curlevel) * (right - left + 1)
                curlevel = curmin
            if A[left] < A[right]:
                block += A[left]
                left += 1
            else:
                block += A[right]
                right -= 1

        return total - block


if __name__ == '__main__':
    s = Solution()
    assert 6 == s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
