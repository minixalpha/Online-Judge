#!/usr/bin/env python
#coding: utf-8

class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        result = []
        
        curL, curW = -1, []
        for wd in words:
            preL = curL
            curL += (len(wd) + 1)
            if curL > L:
                result.append((curW, preL-len(curW)+1))
                curL = len(wd)
                curW = []
            curW.append(wd)
        result.append((curW, curL-len(curW)+1))

        final = []
        for i in range(len(result)):
            line, length = result[i]
            if len(line) > 1 and i != len(result) - 1:
                avg, remain = divmod(L-length, len(line) - 1)
                curR = []
                for i in range(len(line)-1):
                    line[i] = line[i] + ' ' * avg
                for i in range(remain):
                    line[i] = line[i] + ' '
                for i in range(len(line)-1):
                    curR.append(''.join(line[i]))
                curR.append(line[-1]) 
                final.append(''.join(curR))
            else:
                cline = ' '.join(line)
                cline = cline + ' ' * (L - len(cline))
                final.append(cline)

        return final

if __name__ == '__main__':
    s = Solution()
    L = ["This", "is", "an", "example", "of", "text", "justification."]
    print(s.fullJustify(L, 16))
    L = ["This", "is"]
    print(s.fullJustify(L, 5))
    L = ["This"]
    print(s.fullJustify(L, 5))
    L = [""]
    print(s.fullJustify(L, 2))
    L = ["What","must","be","shall","be."]
    print(s.fullJustify(L, 12))
