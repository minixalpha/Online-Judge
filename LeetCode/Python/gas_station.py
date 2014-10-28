#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        total, tank, start = 0, 0, 0
        lg = len(gas)

        for i in range(lg):
            tank = tank + gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                total += tank
                tank = 0
        return start if total + tank >= 0 else -1

if __name__ == '__main__':
    s = Solution()
    assert -1 == s.canCompleteCircuit([0], [1])
    assert 0 == s.canCompleteCircuit([1], [0])
    assert 0 == s.canCompleteCircuit([2, 1], [1, 2])
    assert -1 == s.canCompleteCircuit([2, 1], [2, 2])
    assert 1 == s.canCompleteCircuit([2, 2], [3, 1])
