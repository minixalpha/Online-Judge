#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        ls, lt = len(S), len(T)
        if ls == 0 or lt == 0: return 0

        distinct = [[0] * ls for i in range(lt)]
        num = 0
        for j in range(0, ls):
            if T[0] == S[j]: num += 1
            distinct[0][j] = num

        for i in range(1, lt):
            for j in range(1, ls):
                use_j = distinct[i-1][j-1] if T[i] == S[j] else 0
                distinct[i][j] = use_j + distinct[i][j-1]

        return distinct[lt-1][ls-1]


if __name__ == '__main__':
    s = Solution()
    assert 1 == s.numDistinct("ABCDE", "ACE")
    assert 3 == s.numDistinct("rabbbit", "rabbit")
    assert 0 == s.numDistinct("fff", "ffff")
