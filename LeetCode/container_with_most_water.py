#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @return an integer
    def maxArea(self, height):
        low, high = 0, len(height) - 1
        max_area = 0
        while low < high:
            max_area = max(max_area, 
                    (high - low) * min(height[low], height[high]))
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
        return max_area
