#!/usr/bin/env python
#coding: utf-8

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return repr((self.start, self.end))

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x: x.start)
        result = []

        i, li = 0, len(intervals)
        while i < li - 1:
            start = intervals[i].start
            end = intervals[i].end
            while i < li - 1 and intervals[i+1].start <= end:
                end = max(end, intervals[i+1].end)
                i += 1
            result.append(Interval(start, end))
            i += 1
        
        if i == li - 1:
            result.append(intervals[i])
        return result


def test(s, lt):
    t = [Interval(x,y) for x, y in lt]
    r = s.merge(t)
    print(r)

if __name__ == '__main__':
    s = Solution()
    test(s, [[1,3],[2,6],[8,10],[15,18]])
    test(s, [[1,4],[2,5]])
    test(s, [[1,4],[4,5]])
    test(s, [[1,4],[2,3]])
    test(s, [[1,4],[1,5]])
    test(s, [[2,3],[4,5],[6,7],[8,9],[1,10]])
