#!/usr/bin/env python
#coding: utf-8

class Solution:
    def _wb(self, s, start, dict, cache):
        if start in cache: return cache[start]
        if start == len(s): return [[]]

        result = []
        i, ls = start+1, len(s)

        while i <= ls:
            if s[start:i] in dict:
                sub_result = self._wb(s, i, dict, cache)
                if sub_result:
                    for sr in sub_result:
                        result.append([s[start:i]] + sr)
            i += 1
        if result == []: result = None
        cache[start] = result
        return result 

    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        result = self._wb(s, 0, dict, {})
        if result == None: return []
        else: return map(lambda x: ' '.join(x), result)


if __name__ == '__main__':
    s = Solution()
    print(s.wordBreak(
        'catsanddog', ["cat", "cats", "and", "sand", "dog"]))
    print(s.wordBreak('a', []))
