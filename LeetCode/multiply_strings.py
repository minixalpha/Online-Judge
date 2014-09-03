#!/usr/bin/env python
#coding: utf-8

class Solution:

    def _mulsingle(self, inum, n, zn):
        result = [0] * zn
        
        c, r = 0, 0
        for i in inum:
            mul = i * n + c
            c, r = mul / 10, mul % 10
            result.append(r)
        
        if c:
            result.append(c)
        return result

    def _add(self, inum1, inum2):
        if not inum1: return inum2
        if not inum2: return inum1

        i, j = 0, 0
        n1, n2 = len(inum1), len(inum2)
        
        num = []
        c = 0
        while i < n1 and j < n2:
            sm = inum1[i] + inum2[j] + c
            c, r = sm / 10, sm % 10
            num.append(r)
            i += 1
            j += 1
        
        while i < n1:
            sm = inum1[i] + c
            c, r = sm / 10, sm % 10
            num.append(r)
            i += 1

        while j < n2:
            sm = inum2[j] + c
            c, r = sm / 10, sm % 10
            num.append(r)
            j += 1

        if c:
            num.append(c)

        return num

    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        inum1 = map(int, num1)
        inum2 = map(int, num2)

        if len(inum1) < len(inum2):
            shortn, longn = inum1[::-1], inum2[::-1]
        else:
            shortn, longn = inum2[::-1], inum1[::-1]

        result = []
        for i in range(len(shortn)):
            cr = self._mulsingle(longn, shortn[i], i)
            result = self._add(result, cr)

        tr = ''.join(map(str,result[::-1]))
        i, ltr = 0, len(tr)
        while i < ltr:
            if tr[i] != '0':
                break
            i += 1
        if i == ltr: return '0'
        else: return tr[i:]


if __name__ == '__main__':
    s = Solution()
    assert '144' == s.multiply('12', '12')
    assert '0' == s.multiply('0', '12')
