#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        n = [0,0,0]
        for i in A:
            n[i] += 1
        
        j = 0
        for k in range(0,3):
            m = 0
            while m < n[k]:
                A[j] = k
                m, j = m + 1, j + 1
        print(A)

if __name__ == '__main__':
    s = Solution()
    s.sortColors([1,0,1,2,0,1,2,1])
