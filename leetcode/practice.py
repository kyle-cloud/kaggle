# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        ans = []
        small, big = 1, 2
        mid = tsum >> 1
        curSum = 3
        res = [small, big]
        while small <= mid:
            print(curSum, res, ans)
            if curSum >= tsum:
                if curSum == tsum: ans.append(res.copy())
                curSum -= small
                small += 1
                res.pop(0)
            elif curSum < tsum:
                big += 1
                curSum += big
                res.append(big)
        return ans