#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        similar = {}

        for str in strs:
            lstr = list(str)
            lstr.sort()
            key = ''.join(lstr)
            if not key in similar:
                similar[key] = []
            similar[key].append(str)


        result = []
        for key in similar:
            if len(similar[key]) > 1:
                result.extend(similar[key])
        return result



if __name__ == '__main__':
    s = Solution()
    assert [] == s.anagrams("")
    assert [] == s.anagrams("a")
    assert ["and", "nad"] == s.anagrams(["and", "nad"])
    assert ["", ""] == s.anagrams(["", ""])
    assert ["and","dan","tea","ate","eat"] == ["and","dan","tea","ate","eat"]
