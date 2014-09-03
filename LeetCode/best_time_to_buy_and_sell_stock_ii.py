#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        total = 0
        n = len(prices)
        for i in range(n-1):
            d = prices[i+1] - prices[i]
            if d >= 0: total += d
        return total



if __name__ == '__main__':
    s = Solution()
    assert 0 == s.maxProfit([])
    assert 0 == s.maxProfit([1, 0])
    assert 1 == s.maxProfit([0, 1])
    assert 3 == s.maxProfit([0, 1, 2, 3])
    assert 0 == s.maxProfit([3, 2, 1, 0])
