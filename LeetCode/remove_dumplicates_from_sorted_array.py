#!/usr/bin/env python
#coding: utf-8


class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A: return 0
        i, j, la = 0, 1, len(A)
        while j < la:
            while j < la and A[i] == A[j]:
                j += 1
            if j < la:
                A[i + 1] = A[j]
                i, j = i + 1, j + 1
        return i + 1


if __name__ == '__main__':
    A = [1, 1, 2, 2, 3]
    s = Solution()
    print(s.removeDuplicates(A))

