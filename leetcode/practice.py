# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n < 0: return False
        if n == 0: return 0
        
        flag = 1
        ans = 0
        s = str(n)
        length = len(s)
        for i in range(length):
            if i == length - 1:
                number = int(s[:length-1])
                if int(s[i]) >= flag: number += 1
                ans += number
            elif i == 0:
                number = int(s[1:])
                if int(s[i]) >= flag: number += 1
                ans += number
            else:
                number_left = int(s[:i])
                number_right = int(s[i+1:])
                if int(s[i]) < flag:
                    ans += number_left * (pow(10, length - i - 1))
                elif int(s[i]) == flag:
                    ans += number_left * (pow(10, length - i - 1))
                    ans += numebr_right + 1
        return ans