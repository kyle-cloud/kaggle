# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def __init__(self):
        self.ans = []
        
    def FindPath(self, root, expectNumber):
        # write code here
        if root == None: return False
        
        self.DFS(root, expectNumber, [root], root.val)
        return self.ans
    
    def DFS(self, root, expectNumber, path, curNumber):
        if root.left == None and root.right == None:
            if curNumber == expectNumber:
                self.ans.append(path)
            return
        
        if root.left: self.DFS(root.left, expectNumber, path + [root.left], curNumber + root.left.val)
        if root.right: self.DFS(root.right, expectNumber, path + [root.right], curNumber + root.right.val)