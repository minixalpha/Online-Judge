#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0: return False
        tx = x
        rx = 0
        while tx > 0:
            rx = 10 * rx + tx % 10
            if rx < 0: return False
            tx /= 10
        return rx == x

if __name__ == '__main__':
    s = Solution()
    assert False == s.isPalindrome(-1)
    assert True == s.isPalindrome(1)
    assert False == s.isPalindrome(12)
    assert True == s.isPalindrome(121)
    assert True == s.isPalindrome(1221)
    assert True == s.isPalindrome(12321)
    assert False == s.isPalindrome(123421)
    assert False == s.isPalindrome(10000021)
