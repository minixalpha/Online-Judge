#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        ln = len(num) - 1
        i, j = ln - 1, ln

        while i >= 0 and num[i] >= num[j]:
            i -= 1
            j -= 1
        if i >= 0:
            k = ln
            while k >= j:
                if num[k] > num[i]:
                    num[k], num[i] = num[i], num[k]
                    break
                k -= 1
            while k < ln:
                if num[k] < num[k+1]:
                    num[k], num[k+1] = num[k+1], num[k]
                    k += 1
                else:
                    break
            num[j:] = num[j:][::-1]
        else:
            num = num[::-1]

        return num

if __name__ == '__main__':
    s = Solution()
    assert [1,3,2] == s.nextPermutation([1,2,3])
    assert [1,2,3] == s.nextPermutation([3,2,1])
    assert [1,5,1] == s.nextPermutation([1,1,5])
    assert [] == s.nextPermutation([])
    assert [2,1,3] == s.nextPermutation([1,3,2])
    assert [3,1,2] == s.nextPermutation([2,3,1])
