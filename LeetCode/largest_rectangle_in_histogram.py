#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        curS, maxS, stack = 0, 0, []

        i, lh = 0, len(height)
        while i < lh:
            if not stack or height[stack[-1]] <= height[i]:
                stack.append(i)
                i += 1
            else:
                tp = stack.pop()

                curS = height[tp] * (i if not stack else i - stack[-1]-1)
                maxS = max(maxS, curS)

        while stack:
            tp = stack.pop()
            curS = height[tp] * (i if not stack else (i - stack[-1] - 1))
            maxS = max(maxS, curS)
        return maxS

if __name__ == '__main__':
    s = Solution()

    assert 12 == s.largestRectangleArea([6,2,5,4,5,1,6])
