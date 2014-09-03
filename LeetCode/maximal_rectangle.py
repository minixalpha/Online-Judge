#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if not matrix: return 0

        rowN, colN = len(matrix), len(matrix[0])
        height = [0] * colN
        stack = []
        i, maxS = 0, 0
        
        while i < rowN:
            j = 0
            while j < colN:
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0

                while stack and height[j] < height[stack[-1]]:
                    tp = stack.pop()
                    curS = height[tp] * (j if not stack 
                            else (j - stack[-1] - 1))
                    maxS = max(maxS, curS)

                stack.append(j)
                j += 1

            while stack:
                tp = stack.pop()
                curS = height[tp] * (j if not stack 
                        else (j - stack[-1] - 1))
                maxS = max(maxS, curS)
            i += 1

        return maxS

if __name__ == '__main__':
    s = Solution()
    assert 0 == s.maximalRectangle("")
    assert 0 == s.maximalRectangle(["", ""])
    assert 1 == s.maximalRectangle(["01", "00"])
    assert 2 == s.maximalRectangle(["11", "00"])
    assert 2 == s.maximalRectangle(["11", "10"])
    assert 4 == s.maximalRectangle(["11", "11"])
    assert 1 == s.maximalRectangle(["1"])
    assert 12 == s.maximalRectangle(
            ["0010","1111","1111","1110","1100","1111","1110"])
    assert 9 == s.maximalRectangle(
            ["01101","11010","01110","11110","11111","00000"])
