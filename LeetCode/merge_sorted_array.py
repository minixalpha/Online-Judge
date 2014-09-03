#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        i, j = 0, 0
        while i < m and j < n:
            if i < m and A[i] <= B[j]:
                i += 1
            else:
                k = j
                while k < n and B[k] < A[i]:
                    k += 1
                
                mn = k - j
                q = m - 1
                while q >= i:
                    A[q + mn] = A[q]
                    q -= 1
                m += mn

                while j < k:
                    A[i] = B[j]
                    i, j = i + 1, j + 1
        while j < n:
            A[i] = B[j]
            i, j = i + 1, j + 1


if __name__ == '__main__':
    s = Solution()
    A = [1,2,3,4,5,0,0,0]
    B = [3,7,9]
    s.merge(A, 5, B, len(B))
    print(A)
