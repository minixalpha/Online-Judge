#!/usr/bin/env python
#coding: utf-8

class Solution:
    def isNumeric(self, t):
        if t[0] == '-':
            t = t[1:]
        return t.isdigit()

    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        q = []
        for t in tokens:
            if self.isNumeric(t):
                if t[0] != '-':
                    q.append(int(t))
                else:
                    q.append(int(t[1:]) * -1)
            else:
                a = q.pop()
                b = q.pop()
                if t == "+":
                    q.append(b + a)
                elif t == "-":
                    q.append(b - a)
                elif t == "*":
                    q.append(b * a)
                elif t == "/":
                    sign = 1
                    if a * b < 0:
                        b = -b
                        sign = -1
                    q.append(sign * (b / a))

        return q[0]


if __name__ == '__main__':
    s = Solution()
    assert s.evalRPN(["3", "-4", "+"]) == -1
    assert s.evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert s.evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert s.evalRPN(["10","6","9","3","+","-11","*",
        "/","*","17","+","5","+"]) == 22
