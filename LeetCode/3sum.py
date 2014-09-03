#!/usr/bin/env python
#coding: utf-8

class Solution:
    def _twosum(self, num, s, e, target):
        i, j = s, e
        r = []
        while i < j:
            sum = num[i] + num[j]
            if sum == target:
                k = (num[i], num[j])
                if not r or (not r[-1] == k):
                    r.append(k)
                i += 1
                j -= 1
            elif sum < target: 
                i += 1
            else:
                j -= 1
        return r

    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        ln = len(num)
        if ln < 3: return []
        i = 0
        r = []
        while i <= ln-3:
            if i > 0 and num[i] == num[i-1]: 
                i += 1
                continue
            x = self._twosum(num, i+1, ln-1, -num[i])
            if x:
                y = [ [num[i], z[0], z[1]] for z in x ]
                for j in y:
                    if not r or not(r[-1] == j):
                        r.append(j)
            i += 1
        return r

if __name__ == '__main__':
    s = Solution()
    assert [[-1,-1,2],[-1,0,1]] == s.threeSum([-1,0,1,2,-1,-4])
    assert [[-2,0,2], [-2,1,1]] == s.threeSum([-2,0,1,1,2])
    assert [[0,0,0]] == s.threeSum([0 for i in range(100)])
    assert [[-2, 0, 2], [-2, 1, 1]] == s.threeSum([-2,-2,0,1,1,2])
