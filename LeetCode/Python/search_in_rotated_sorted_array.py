#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        start, end = 0, len(A) - 1

        while start <= end:
            mid = start + (end - start) / 2
            if A[mid] == target: return mid
            if A[start] <= A[mid]:
                if target < A[mid] and target >= A[start]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target > A[mid] and target <= A[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1

if __name__ == '__main__':
    s = Solution()
    assert -1 == s.search([4,5,6,7,0,1,2], -2)
    assert -1 == s.search([4,5,6,7,0,1,2], 8)
    assert 4 == s.search([4,5,6,7,0,1,2], 0)
    assert 0 == s.search([4,5,6,7,0,1,2], 4)
    assert 1 == s.search([1,3], 3)
