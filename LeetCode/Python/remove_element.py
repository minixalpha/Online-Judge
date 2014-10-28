#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        i, la = 0, len(A)
        while i < la:
            while i < la and A[i] != elem:
                i += 1
            if i == la: break

            j = i
            while j < la and A[j] == elem:
                j += 1
            
            rm_n = j - i
            for k in range(j, la):
                A[k - rm_n] = A[k]

            la -= rm_n
        return la


if __name__ == '__main__':
    A = [1, 2, 3, 3, 4, 3, 5, 3, 3]
    s = Solution()
    print(s.removeElement(A, 3))
    print(A)

