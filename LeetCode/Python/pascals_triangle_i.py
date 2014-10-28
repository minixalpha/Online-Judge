#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @return a list of lists of integers
    def generate(self, rowIndex):
        if not rowIndex: return [1]

        i, c, bc = 1, [1], [1]
        while i <= rowIndex:
            c, j, lbc = [1], 0, len(bc) - 1
            while j < lbc:
                c.append(bc[j] + bc[j+1])
                j += 1
            c.append(1)
            bc, i = c, i + 1

        return c

if __name__ == '__main__':
    s = Solution()

    print(s.generate(0))
    print(s.generate(1))
