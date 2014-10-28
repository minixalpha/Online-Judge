#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        stack, record = [], []
        for e in zip(range(len(s)), s):
            if not stack or e[1] == '(':
                stack.append(e)
                continue
            elif stack[-1][1] == '(':
                te = stack.pop()
                record.append((te[0], e[0]))
        
        if not record: return 0
        record.sort()
        tmax, cmax = 2, 2
        start, end = record[0]
        for i in range(1, len(record)):
            if (record[i][0] == end + 1 or
                record[i][1] < end):
                cmax += 2
                end = max(end, record[i][1])
            else:
                tmax = max(tmax, cmax)
                cmax = 2
                start, end = record[i]
        return max(tmax, cmax)

if __name__ == '__main__':
    s = Solution()
    assert 0 == s.longestValidParentheses('')
    assert 0 == s.longestValidParentheses('(')
    assert 0 == s.longestValidParentheses(')')
    assert 0 == s.longestValidParentheses('))')
    assert 0 == s.longestValidParentheses(')(')
    assert 0 == s.longestValidParentheses('((')
    assert 2 == s.longestValidParentheses('(()')
    assert 4 == s.longestValidParentheses(')()())')
    assert 6 == s.longestValidParentheses(')()())()()()')
    assert 6 == s.longestValidParentheses(')()())((()))')
    assert 2 == s.longestValidParentheses('()(()')
    assert 6 == s.longestValidParentheses('()(())')
    assert 8 == s.longestValidParentheses('((()))())')
