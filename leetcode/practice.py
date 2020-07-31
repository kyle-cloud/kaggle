# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        # None None singleline allthesame
        for i in range(rows):
            for j in range(cols):
                if self.DFS(list(matrix), rows, cols, i, j, path):
                     return True
        return False
    
    def DFS(self, matrix, rows, cols, row, col, path):
        #! path out of index
        if not path: return True
        if 0 <= row < rows and 0 <= col < cols and matrix[row*cols+col] == path[0]:
            matrix[row*cols+col] = '0'
            for [i, j] in self.directions:
                if self.DFS(matrix, rows, cols, row+i, col+j, path[1:]):
                    #print(matrix) matrix已经被改变了，数据集有问题，应该加上回溯才对
                    return True
        return False