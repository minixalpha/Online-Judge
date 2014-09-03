#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        for x in s:
            if x == '(' or x == '{' or x == '[':
                stack.append(x)
            else:
                if not stack: return False
                y = stack.pop()
                if x == ')' and y != '(': return False
                if x == ']' and y != '[': return False
                if x == '}' and y != '{': return False
        if not stack: return True
        return False

if __name__ == '__main__':
    s = Solution()
    assert True == s.isValid('()')
    assert True == s.isValid('()[]{}')
    assert False == s.isValid('(]')
    assert False == s.isValid('([)]')

