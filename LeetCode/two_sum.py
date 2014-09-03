#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        ln = len(num)
        tnum = [(num[i], i+1) for i in range(ln)]
        tnum.sort()
        i, j = 0, ln - 1

        while i < j:
            s = tnum[i][0] + tnum[j][0]
            if s > target:
                j -= 1
            elif s < target:
                i += 1
            else:
                x, y = tnum[i][1], tnum[j][1]
                return (min(x,y), max(x,y))
        return (0, 0)


if __name__ == '__main__':
    s = Solution()
    assert (1, 2) == s.twoSum([2, 7, 11, 15], 9)
    assert (2, 3) == s.twoSum([3,2,4], 6)
    assert (2, 3) == s.twoSum([5,75,25], 100)
