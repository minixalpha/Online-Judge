#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @return a string
    def longestPalindrome(self, s):
        T = '#' + '#'.join(list(s)) + '#'
        P = [0] * len(T)
        C, R = 0, 0
        for i in range(1, len(T)-1):
            mi = C - (i - C)
            if R > i:
                P[i] = min(R - i, P[mi])

            ri, li = i + P[i] + 1, i - P[i] - 1
            while (li >= 0 and ri < len(T) and 
                    T[li] == T[ri]
                    ):
                P[i] += 1
                ri, li = i + P[i] + 1, i - P[i] - 1

            if i + P[i] > R:
                C = i
                R = i + P[i]
        
        maxLen, centerI = 0, 0
        for i in range(1, len(P) - 1):
            if P[i] > maxLen:
                maxLen = P[i]
                centerI = i


        start = (centerI - maxLen) / 2
        end = start + maxLen
        return s[start:end]

if __name__ == '__main__':
    s = Solution()
    assert 'a' == s.longestPalindrome('a')
    assert 'aa' == s.longestPalindrome('aa')
    assert 'aba' == s.longestPalindrome('aba')
    assert 'abaaba' == s.longestPalindrome('abaaba')
    assert 'cc' == s.longestPalindrome('ccd')
