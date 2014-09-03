#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        n = len(prices)
        if n < 2: return 0

        before_p = [0] * n
        after_p = [0] * n
        
        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            before_p[i] = max(before_p[i-1], prices[i] - min_price)

        max_price = prices[n-1]
        mp = 0
        for i in range(n-2, -1, -1):
            max_price = max(max_price, prices[i])
            after_p[i] = max(after_p[i+1], max_price - prices[i])
            mp = max(mp, after_p[i] + before_p[i])
        return mp


if __name__ == '__main__':
    s = Solution()
    assert 0 == s.maxProfit([1])
    assert 0 == s.maxProfit([2, 1])
    assert 1 == s.maxProfit([1, 2])
    assert 2 == s.maxProfit([1, 2, 3])
