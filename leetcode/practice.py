# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        # +/-A[.B][e|E C]
        # +/-.B[w|E C]
        if s == None or len(s) == 0: return False
        
        index = 0
        if s[0] == '+' or s[0] == '-': 
            index += 1
        #A
        index = self.scan(s, index)
        #.B
        if index < len(s) and s[index] == '.':
            index += 1
            index = self.scan(s, index)
        #e|E C
        if index < len(s) and (s[index] == 'E' or s[index] == 'e'):
            index += 1
            if index < len(s) and s[index] == '+' or s[index] == '-': 
                index += 1
            index = self.scan(s, index)
        
        return True if index == len(s) else False
     
    def scan(self, s, index):
        while index < len(s):
            if s[index] < '0' or s[index] > '9':
                break
            index += 1
        return index