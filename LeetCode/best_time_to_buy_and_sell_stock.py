#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):#
        if not prices: return 0

        n = len(prices)
        min_p = prices[0]
        max_profict = 0
        for i in range(1, n):
            if prices[i] < min_p:
                min_p = prices[i]
            cur_profit = prices[i] - min_p
            if cur_profit > max_profict:
                max_profict = cur_profit

        return max_profict
        

if __name__ == '__main__':
    s = Solution()
    assert 0 == s.maxProfit([1])
    assert 1 == s.maxProfit([1, 2])
    assert 0 == s.maxProfit([2, 1])
    assert 8 == s.maxProfit([1,3,9])
