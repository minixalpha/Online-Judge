#!/usr/bin/env python
#coding: utf-8


class Solution:
    # @return a string
    def intToRoman(self, num):
        int_roman = [
                (1000, 'M'),
                (900, 'CM'),
                (500, 'D'),
                (400, 'CD'),
                (100, 'C'),
                (90, 'XC'),
                (50, 'L'),
                (40, 'XL'),
                (10, 'X'),
                (9, 'IX'),
                (5, 'V'),
                (4, 'IV'),
                (1, 'I')
                ]
        rl = []
        while num > 0:
            for r, m in int_roman:
                if r <= num:
                    rl.append(m)
                    num -= r
                    break
        return ''.join(rl)


if __name__ == '__main__':
    s = Solution()
    assert 'MCMXC' == s.intToRoman(1990)
