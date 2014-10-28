#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        ls1, ls2 = len(s1), len(s2)
        if ls1 != ls2: return False
        cs1, cs2 = list(s1), list(s2)
        cs1.sort(), cs2.sort()
        if cs1 != cs2: return False

        if s1 == s2: return True

        ls = ls1
        for i in range(1, ls):
            s1_sub1, s1_sub2 = s1[:i], s1[i:]
            s2_sub1, s2_sub2 = s2[:i], s2[i:]
            s3_sub1, s3_sub2 = s2[ls-i:], s2[:ls-i]

            if (self.isScramble(s1_sub1, s2_sub1) and 
                self.isScramble(s1_sub2, s2_sub2)):
                return True
            if (self.isScramble(s1_sub1, s3_sub1) and 
                self.isScramble(s1_sub2, s3_sub2)):
                return True

        return False

if __name__ == '__main__':
    s = Solution()
    assert True == s.isScramble("great", "rgeat")
    assert True == s.isScramble("great", "rgtae")
    assert True == s.isScramble("great", "taerg")
