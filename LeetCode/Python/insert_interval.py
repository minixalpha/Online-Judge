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
    def _merge(self, intervals):
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

    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        result = self._merge(intervals)
        return result

def test(s, lt, ni):
    t = [Interval(x,y) for x, y in lt]
    r = s.insert(t, Interval(ni[0], ni[1]))
    print(r)

if __name__ == '__main__':
    s = Solution()
    test(s, [[1,3],[6,9]], [2,5])

    test(s, [[1,2],[3,5],[6,7],[8,10],[12,16]], [4,9])
