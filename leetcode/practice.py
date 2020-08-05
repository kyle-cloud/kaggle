# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.ans = []
    
    def Permutation(self, ss):
        # write code here
        if not ss: return []
        
        self.DFS(ss, '')
        return self.ans
    
    def DFS(self, s, res):
        
        if s == "":
            print(s + '1' + res)
            self.ans.append(res)
            return
        
        for i in range(len(s)):
            self.DFS(s[:i] + s[i+1:], res + s[i])
        