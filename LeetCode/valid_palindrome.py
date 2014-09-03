#!/usr/bin/env python
#coding: utf-8

class Solution:
    def isalphanumeric(self, c):
        return c.isalpha() or unicode(c).isnumeric()
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        yes = True
        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not self.isalphanumeric(s[i]):
                i += 1
            while i < j and not self.isalphanumeric(s[j]):
                j -= 1
            if i < j and s[i].lower() != s[j].lower():
                yes = False
                break
            i += 1
            j -= 1
        return yes

if __name__ == '__main__':
    s = Solution()
    assert True == s.isPalindrome('')
    assert False == s.isPalindrome('race a car')
    assert True == s.isPalindrome('A man, a plan, a canal: Panama')
    assert False == s.isPalindrome('1a2')
