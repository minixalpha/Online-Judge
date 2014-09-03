#!/usr/bin/env python
#coding: utf-8

class Solution:
    def reverseWords(self, s):
        rs = s.split(' ')
        rs = [t for t in rs if len(t) > 0]
        return ' '.join(rs[::-1])

if __name__ == "__main__":
    s = Solution()
    print(s.reverseWords(" "))
