#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        if s == p: return True
        if not s and not p: return True  
        if not s and p[0] == '*': return self.isMatch(s, p[1:])
        if not s and p[0] != '*': return False
        if s and not p: return False

        if s[0] == p[0]: return self.isMatch(s[1:], p[1:])
        if p[0] == '?': return self.isMatch(s[1:], p[1:])
        if p[0] == '*':
            k, lp, ls = 0, len(p), len(s)
            while k < lp and p[k] == '*':
                k += 1
            if k == lp: return True
            ret = False
            for i in range(ls + 1):
                ci, ck = i, k
                while ci < ls and ck < lp and (s[ci] == p[ck] or p[ck] == '?'):
                    ci += 1
                    ck += 1
                if ci == ls and ck == lp: return True

                if ck < lp and p[ck] == '*':
                    ret = self.isMatch(s[ci:], p[ck:])
                    # if ret == True, find a match
                    # if ret == False, then the result must be False
                    # reason: if f1f2 AB !match *f1f2 *C
                    #         then f2A B !match f1f2 *C
                    #   reason: if AB !match *C
                    #           then B !match *C
                    return ret
                if ci == ls: return False
            return ret
        return False


if __name__ == '__main__':
    s = Solution()
    assert False == s.isMatch("aa", "a")
    assert True == s.isMatch("aa", "aa")
    assert False == s.isMatch("aaa", "aa")
    assert True == s.isMatch("aa", "*")
    assert True == s.isMatch("aa", "a*")
    assert True == s.isMatch("ab", "?*")
    assert False == s.isMatch("aab", "c*a*b")
    assert False == s.isMatch('babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab', '***bba**a*bbba**aab**b')
    assert False == s.isMatch(
            'bbaaaaaabbbbbabbabbaabbbbababaaabaabbababbbabbababbaba', 
            'b*b*ba**a*aaa*a*b**bbaa')
