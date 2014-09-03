#!/usr/bin/env python
#coding: utf-8

class Solution:
    def _findk(self, A,  B, k):
        if len(A) > len(B): return self._findk(B, A, k)
        if len(A) == 0: return B[k-1]
        if k == 1: return min(A[0], B[0])

        ia = min(k / 2, len(A))
        ib = k - ia
        
        if A[ia - 1] == B[ib - 1]:
            return A[ia - 1]
        elif A[ia - 1] < B[ib - 1]:
            return self._findk(A[ia:], B, k-ia)
        else:
            return self._findk(A, B[ib:], k-ib)

    # @return a float
    def findMedianSortedArrays(self, A, B):
        total = len(A) + len(B)
        if total % 2 != 0:
            return self._findk(A, B, total / 2 + 1)
        else:
            return (self._findk(A, B, total / 2) 
                  + self._findk(A, B, total / 2 + 1)) / 2.0

if __name__ == '__main__':
    s = Solution()

    assert 1 == s.findMedianSortedArrays([1], [])
    assert 2 == s.findMedianSortedArrays([1, 2, 3], [])
    assert 1.5 == s.findMedianSortedArrays([1, 2], [])

    assert 1 == s.findMedianSortedArrays([], [1])
    assert 2 == s.findMedianSortedArrays([], [1, 2, 3])
    assert 1.5 == s.findMedianSortedArrays([], [1, 2])

    assert 1 == s.findMedianSortedArrays([1], [1])
    assert 1 == s.findMedianSortedArrays([1], [1, 2])
    assert 2 == s.findMedianSortedArrays([1, 2], [2])
    assert 2 == s.findMedianSortedArrays([2], [1, 2])
    assert 1.5 == s.findMedianSortedArrays([1, 2], [1, 2])
    assert 2 == s.findMedianSortedArrays([1,2],[1,2,3])
    assert 2 == s.findMedianSortedArrays([1], [2,3])
    assert 2 == s.findMedianSortedArrays([3], [1,2])
    assert 2.5 == s.findMedianSortedArrays([2,3,4], [1])
