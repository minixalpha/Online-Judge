#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        lr = len(ratings)
        if lr <= 1: return lr

        cd = [0 for i in range(lr)]
        if ratings[0] <= ratings[1]: cd[0] = 1
        if ratings[lr-1] <= ratings[lr-2]: cd[lr-1] = 1
        for i in range(1, lr-1):
            if ratings[i-1] >= ratings[i] and ratings[i+1] >= ratings[i]:
                cd[i] = 1

        for i in range(lr):
            if cd[i] == 1:
                j = i - 1
                while j >= 0:
                    if ratings[j] == ratings[j+1]:
                        tcd = 1
                    elif ratings[j] > ratings[j+1]:
                        tcd = cd[j+1] + 1
                    else:
                        break
                    cd[j] = max(cd[j], tcd)
                    j -= 1
                j = i + 1
                while j < lr:
                    if ratings[j] == ratings[j-1]:
                        tcd = 1
                    elif ratings[j] > ratings[j-1]:
                        tcd = cd[j-1] + 1
                    else:
                        break
                    cd[j] = max(cd[j], tcd)
                    j += 1

        return sum(cd)


if __name__ == '__main__':
    s = Solution()
    assert 3 == s.candy([1,1,1])
    assert 4 == s.candy([1,2,1])
    assert 6 == s.candy([3,2,1])
    assert 6 == s.candy([1,2,3])
    assert 4 == s.candy([1,2,2])
    assert 15 == s.candy([5,1,1,1,10,2,1,1,1,3])
