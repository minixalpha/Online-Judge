#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        ld = len(digits) - 1
        while ld >= 0:
            digits[ld] += 1
            if digits[ld] < 10:
                break
            else:
                digits[ld] -= 10
            ld -= 1
        if ld < 0:
            return [1] + digits
        else:
            return digits

if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([0,0]))
    print(s.plusOne([0,9]))
    print(s.plusOne([1,9]))
    print(s.plusOne([9,9]))
