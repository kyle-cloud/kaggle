# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.minus = 1 #-1
        self.g_valid = False
        
    def StrToInt(self, s):
        # write code here
        # None "" + a overflow
        if not s: self.g_valid = False; return 0
        if len(s) == 1 and (s[0] == '+' or s[0] == '-'):
            self.g_valid = False; return
        
        num = 0
        index = 0
        if s[index] == '+':
            index += 1
            self.minus = 1
        elif s[index] == '-':
            index += 1
            self.minus = -1
        
        while index < len(s):
            if s[index] < '0' or s[index] > '9':
                self.g_valid = False
                return
            num = num * 10 + self.minus * int(s[index])
            if num > 0x7FFFFFFF or num < 0x80000000:
                index += 1
            else:
                self.g_valid = False
                return
        return num