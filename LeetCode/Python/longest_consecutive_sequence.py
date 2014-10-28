#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        section = {}
        longest_len = 0
        for n in num:
            if n in section: continue
            
            low = section.get(n - 1, n)
            high = section.get(n + 1, n)

            section[n] = n
            section[low] = high
            section[high] = low

            longest_len = max(longest_len, high - low + 1)

        return longest_len


if __name__ == '__main__':
    s = Solution()
    assert 4 == s.longestConsecutive([100, 4, 200, 1, 3, 2])
