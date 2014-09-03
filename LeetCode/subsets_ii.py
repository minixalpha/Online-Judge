#!/usr/bin/env python
#coding: utf-8

class Solution:
    def subsets(self, S):
        S.sort()
        result = [[]]
        pre, pos = None, 0
        for s in S:
            if s != pre:
                pre, pos = s, len(result)
            result = result + [r + [s] for r in result[len(result)-pos:]]
        return result


if __name__ == '__main__':
    print(Solution().subsets([1,2,2,2]))
    print(Solution().subsets([1,2,2]))
    print(Solution().subsets([1,2,3]))
