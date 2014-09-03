#!/usr/bin/env python
#coding: utf-8

class Solution:
    def _isEnough(self, ttimes, ctimes):
        for t in ttimes:
            if ttimes[t] > ctimes[t]: return False
        return True

    def _stat(self, S, T):
        ttimes, ctimes = {}, {}
        for t in T:
            if not t in ttimes:
                ttimes[t] = 0
            ttimes[t] += 1
            ctimes[t] = 0
        return ttimes, ctimes
    
    def _findFirstWindow(self, S, T, ttimes, ctimes):
        start, end = 0, 0
        while end < len(S):
            if S[end] in ctimes:
                ctimes[S[end]] += 1
            enough = self._isEnough(ttimes, ctimes)
            if enough: break
            end += 1
        if end == len(S) and not enough: 
            return None, None

        while start < end:
            if S[start] in ctimes:
                if ctimes[S[start]] > ttimes[S[start]]:
                    ctimes[S[start]] -= 1
                else:
                    break
            start += 1
        return start, end

    def _findMinWindow(self, S, T, ttimes, ctimes, start, end):
        mincnt = end - start + 1
        mstart, mend = start, end

        end += 1
        while end < len(S):
            if S[end] in ctimes:
                ctimes[S[end]] += 1
            
                while start < end:
                    if S[start] in ctimes:
                        if ctimes[S[start]] > ttimes[S[start]]:
                            ctimes[S[start]] -= 1
                        else:
                            cnt = end - start + 1
                            if cnt < mincnt:
                                mincnt = cnt
                                mstart, mend = start, end
                            break
                    start += 1
            end += 1
        return mstart, mend

    # @return a string
    def minWindow(self, S, T):
        ttimes, ctimes = self._stat(S, T)
        start, end = self._findFirstWindow(S, T, ttimes, ctimes)
        if start == None: return ''
        mstart, mend = self._findMinWindow(S, T, ttimes, ctimes, start, end)
        return( S[mstart: mend+1])
            
if __name__ == '__main__':
    s = Solution()
    assert 'BANC' == s.minWindow('ADOBECODEBANC', 'ABC')
    assert '' == s.minWindow('a', 'aa')
    assert 'a' == s.minWindow('a', 'a')
    assert 'aa' == s.minWindow('aa', 'aa')
    assert "aec" == s.minWindow('cabefgecdaecf', 'cae')
    assert "ba" == s.minWindow('bba', 'ab')
    assert 'baa' == s.minWindow('bbaac', 'aba')
    assert 'cabd' == s.minWindow('abcabdebac', 'cda')
