#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @return a boolean
    def _isInterleave(self, s1, i, s2, j, s3, k, cache):
        result = None
        if not s1[i:]: 
            result = (s2[j:] == s3[k:])
        elif not s2[j:]: 
            result =  s1[i:] == s3[k:]
        elif not s3[k:]: 
            result = False
        
        if result != None:
            cache[(i, j, k)] = result
            return result

        if (i, j, k) in cache: return cache[(i, j, k)]

        if s1[i] == s3[k]:
            if self._isInterleave(s1, i+1, s2, j, s3, k+1, cache): 
                cache[(i,j,k)] = True
                return True
        if s2[j] == s3[k]:
            if self._isInterleave(s1, i, s2, j+1, s3, k+1, cache): 
                cache[(i,j,k)] = True
                return True
        cache[(i,j,k)] = False
        return False

    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3): return False
        cache = {}
        return self._isInterleave(s1, 0, s2, 0, s3, 0, cache)

if __name__ == '__main__':
    s = Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    s31 = "aadbbcbcac"
    s32 = "aadbbbaccc"
    assert True == s.isInterleave(s1, s2, s31)
    assert False == s.isInterleave(s1, s2, s32)

    s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
    s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
    s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
    assert False == (s.isInterleave(s1, s2, s3))
