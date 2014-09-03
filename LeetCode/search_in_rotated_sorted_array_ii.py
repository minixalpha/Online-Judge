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
            if A[mid] == target: return True
            if A[start] < A[mid]:
                if target < A[mid] and target >= A[start]:
                    end = mid - 1
                else:
                    start = mid + 1
            elif A[start] > A[mid]:
                if target > A[mid] and target <= A[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if start != mid:
                    if A[mid] == A[end]:
                        end = mid - 1
                    else:
                        start = mid + 1
                else:
                    start += 1
        return False

if __name__ == '__main__':
    s = Solution()
    assert False == s.search([4,5,6,7,0,1,2], -2)
    assert False == s.search([4,5,6,7,0,1,2], 8)
    assert True == s.search([4,5,6,7,0,1,2], 0)
    assert True == s.search([4,5,6,7,0,1,2], 4)
    assert True == s.search([1,3], 3)
    assert True == s.search([1,3,1,1,1], 3)
    assert True == s.search([1,1,3], 3)
    assert True == s.search([1,1,3,1], 3)
