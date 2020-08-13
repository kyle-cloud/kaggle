# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s: return -1
        
        dic = {}
        for ch in s:
            if ch not in dic:
                dic[ch] = 1
            else:
                dic[ch] = dic[ch] + 1
        
        for key, value in dic.items():
            if value == 1:
                return s.index(key)
        
        return -1