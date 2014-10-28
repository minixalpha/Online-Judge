#!/usr/bin/env python
#coding: utf-8

class Solution:
    def _next(self, sn):
        i, lsn = 0, len(sn)
        nsn = []
        while i < lsn:
            c = sn[i]
            i += 1
            pi = i
            while i < lsn and c == sn[i]:
                i += 1
            nsn.extend([str(i - pi + 1), c])
        return ''.join(nsn)

    # @return a string
    def countAndSay(self, n):
        n -= 1
        sn = '1'
        while n > 0:
            sn = self._next(sn)
            n -= 1
        return sn

if __name__ == '__main__':
    s = Solution()
    assert '1' == s.countAndSay(1)
    assert '11' == s.countAndSay(2)
    assert '21' == s.countAndSay(3)
    assert '1211' == s.countAndSay(4)
    assert '111221' == s.countAndSay(5)
