#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        r = path.split('/')
        lr = len(r)
        i, tr = 0, []
        while i < lr:
            if r[i] != '':
                if r[i] == '..':
                    if tr:
                        tr.pop()
                elif r[i] != '.':
                    tr.append(r[i])
            i += 1
        return '/' + '/'.join(tr)

if __name__ == '__main__':
    s = Solution()
    assert '/' == s.simplifyPath('///')
    assert '/' == s.simplifyPath('/.')
    assert '/' == s.simplifyPath('/..')
    assert '/home' == s.simplifyPath('/home/')
    assert '/c' == s.simplifyPath('/a/./b/../../c/')
    assert '/a/c' == s.simplifyPath('/a/./b/../c/')
