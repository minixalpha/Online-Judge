#!/usr/bin/env python
#coding: utf-8

import math

class Solution:
    # @return a string
    def getPermutation(self, n, k):
        if k <= 0: return ''

        k -= 1
        nums = range(1, n+1)
        permu = []

        for i in range(n-1, -1, -1):
            chooseI, k = divmod(k, math.factorial(i))
            permu.append(nums.pop(chooseI))

        return ''.join(map(str,permu))


if __name__ == '__main__':
    s = Solution()
    assert "312" == s.getPermutation(3, 5)
