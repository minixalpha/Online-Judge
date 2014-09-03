#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        result = [[]]
        
        n = 0
        for s in num:
            nr = []
            for r in result:
                for i in range(n+1):
                    nr.append(r[:i] + [s] + r[i:])
            result = nr
            n += 1
        return result


if __name__ == '__main__':
    print(Solution().permute([1,2,3]))
