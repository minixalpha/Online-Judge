#!/usr/bin/env python
#coding: utf-8

class Solution:
    def _matchChar(self, a, b):
        if b == '.' or a == b: return True
        else: return False

    def _im(self, s, p, starts, startp, cache):
        if len(p) <= startp: return len(s) == starts
        if (starts, startp) in cache: return cache[(starts,startp)]

        if len(p) == startp + 1 or p[startp+1] != '*':
            if starts >= len(s) or not self._matchChar(s[starts], p[startp]): 
                cache[(starts, startp)] = False
                return False
            else: 
                result = self._im(s, p, starts+1, startp+1, cache)
                cache[(starts, startp)] = result
                return result
        else:
            if self._im(s, p, starts, startp+2, cache): # '*' eat p[0]
                cache[(starts, startp)] = True
                return True
            else:
                i = 0
                while starts+i < len(s) and self._matchChar(s[starts+i], p[startp]):
                    if self._im(s, p, starts+i+1, startp+2, cache):
                        cache[(starts, startp)] = True
                        return True
                    i += 1
                cache[(starts, startp)] = False
                return False

    # @return a boolean
    def isMatch(self, s, p):
        return self._im(s, p, 0, 0, {})

if __name__ == '__main__':
    s = Solution()
    assert True == s.isMatch("aa", "aa")
    assert False == s.isMatch("aa", "a")
    assert False == s.isMatch("aaa", "aa")
    assert True == s.isMatch("aa", "a*")
    assert True == s.isMatch("aa", ".*")
    assert True == s.isMatch("ab", ".*")
    assert True == s.isMatch("aab", "c*a*b")
    assert True == s.isMatch("aaa", "a*a")
    assert False == s.isMatch('aaaaaaaaaaaaab', 'a*a*a*a*a*a*a*a*a*a*c')
    assert True == s.isMatch('a', 'ab*')
    assert False == s.isMatch('ab', '.*c')
