#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        n = len(num)
        if n <= 3: return sum(num)
        num.sort()
        closest = num[0] + num[1] + num[2]
        best = abs(closest - target)
        for i in range(0, n-2):
            j, k = i + 1, n - 1

            while j < k:
                total = num[i] + num[j] + num[k]
                if abs(total - target) < best:
                    best = abs(total - target)
                    closest = total
                if total < target: j += 1
                else: k -= 1
        return closest


if __name__ == '__main__':
    s = Solution()
    assert 2 == s.threeSumClosest([-1,2,1,-4], 1)
    assert 4 == s.threeSumClosest([-1,2,3], 1)
    assert 4 == s.threeSumClosest([-1,2,3,-4], 4)
    assert -3 == s.threeSumClosest([-1,2,3,-4], -3)
    assert -2 == s.threeSumClosest([-1,2,3,-4], -2)
    assert -2 == s.threeSumClosest([-3,-2,-5,3,-4], -1)
