from typing import List
class Solution:
    import sys
    sys.setrecursionlimit(1000000)
    
    def __init__(self):
        self.directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        self.ans = False
    
    def containsCycle(self, grid: List[List[str]]) -> bool:
        if not grid: return False
        if len(grid) == 1: return False

        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j]:
                    self.dfs(grid, visited, i, j, [-1, -1])
                    if self.ans: return True
        return False
    
    def dfs(self, grid, visited, row, col, father):
        visited[row][col] = True
        for i, j in self.directions:
            if 0 <= row + i < len(grid) and 0 <= col + j < len(grid[0]) and (row + i != father[0] or col + j != father[1]) and grid[row + i][col + j] == grid[row][col]:
                if visited[row+i][col+j]:
                    self.ans = True
                    return
                self.dfs(grid, visited, row+i, col+j, [row, col])