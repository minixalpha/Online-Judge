#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A: return 0
        i, j, la = 0, 1, len(A)
        while j < la:
            if A[i] == A[j]:
                A[i+1] = A[j]
                j += 1
                while j < la and A[i] == A[j]:
                    j += 1
                if j < la and j > i + 1:
                    A[i+2] = A[j]
                    i = i + 2
                    j = j + 1
                else:
                    i = i + 1
            else:
                A[i+1] = A[j]
                i = i + 1
                j = j + 1
        return i+1



if __name__ == '__main__':
    assert 5 == Solution().removeDuplicates([1,1,1,2,2,3])
    assert 3 == Solution().removeDuplicates([1,2,3])
    assert 2 == Solution().removeDuplicates([1,1])
    assert 4 == Solution().removeDuplicates([1,1,1,2,3])
