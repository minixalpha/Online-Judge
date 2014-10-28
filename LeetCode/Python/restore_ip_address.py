#!/usr/bin/env python
#coding: utf-8

class Solution:
    def _sp(self, s, ls, n):
        if ls == 0: return []
        maxL = 1 if s[0] == '0' else 3

        if n == 1:
            if ls > 0 and ls <= maxL:
                ints = int(s)
                if ints <= 255 and ints >= 0:
                    return [s]
            return []


        r = []
        for m in range(1, maxL+1):
            if ls >= m:
                ints = int(s[:m])
                if ints <= 255:
                    x = self._sp(s[m:], ls-m, n-1)
                    for i in x:
                        r.append(s[:m] + '.' + i)
        return r

    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        r = self._sp(s, len(s), 4)
        return r


if __name__ == '__main__':
    s = Solution()
    assert (["255.255.11.135", "255.255.111.35"] 
            == s.restoreIpAddresses("25525511135"))
    assert ["1.1.1.1"] == s.restoreIpAddresses("1111")
    assert ["255.255.255.255"] == s.restoreIpAddresses("255255255255")
    assert ["0.10.0.10","0.100.1.0"] == s.restoreIpAddresses("010010")
