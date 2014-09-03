#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if not numRows: return []

        i, bc, r = 1, [1], [[1]]
        while i < numRows:
            c, j, lbc = [1], 0, len(bc) - 1
            while j < lbc:
                c.append(bc[j] + bc[j+1])
                j += 1
            c.append(1)
            r.append(c)
            bc, i = c, i + 1

        return r

if __name__ == '__main__':
    s = Solution()

    print(s.generate(5))
