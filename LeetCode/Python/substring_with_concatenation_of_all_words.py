#!/usr/bin/env python
#coding: utf-8

class Solution:
    def _getWdCount(self, L, length):
        i, wd_count = 0, {}
        while i + length <= len(L): 
            wd = L[i:i+length]
            if not wd in wd_count: wd_count[wd] = 0
            wd_count[wd] += 1
            i += length
        return wd_count

    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        if not L: return []

        count, length = len(L), len(L[0])
        totalL = count * length
        if len(S) < totalL: return []

        result, i = [], 0
        LCount = self._getWdCount(''.join(L), length)
        while i + totalL <= len(S):
            curL = S[i:i+totalL]
            j, curLCount = 0, {}
            while j + length <= len(curL):
                wd = curL[j:j+length]
                if not wd in curLCount: curLCount[wd] = 0
                curLCount[wd] += 1
                if not wd in LCount or curLCount[wd] > LCount[wd]:
                    break
                j += length
            else:
                result.append(i)
            i += 1
        return result

if __name__ == '__main__':
    s = Solution()
    assert [13] == s.findSubstring(
            "lingmindraboofooowingdingbarrwingmonkeypoundcake",
            ["fooo","barr","wing","ding","wing"])
    assert [0, 9] == s.findSubstring(
            "barfoothefoobarman",
            ["foo", "bar"])
    assert [0, 1, 2] == s.findSubstring(
            "aaa",
            ["a"])
    assert [] == s.findSubstring(
            "aaa",
            ["a", "b"])
