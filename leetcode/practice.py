import functools
import time
@functools.lru_cache()

class Solution():
    def __init__(self):
        self.dir = [[1,1,0,1,1,0,0,0,0],
                [1,1,1,0,0,0,0,0,0],
                [0,1,1,0,1,1,0,0,0],
                [1,0,0,1,0,0,1,0,0],
                [0,1,0,1,1,1,0,1,0],
                [0,0,1,0,0,1,0,0,1],
                [0,0,0,1,1,0,1,1,0],
                [0,0,0,0,0,0,1,1,1],
                [0,0,0,0,1,1,0,1,1]
            ]
        self.start = [0] * 9
        self.number = [0] * 9

    def dfs(self, index):
        temp = self.start[:]
        for i in range(9):
            for j in range(9):
                temp[i] = (temp[i] + self.dir[j][i] * self.number[j]) % 4
        if sum(temp) == 0:
            for i in range(9):
                for j in range(self.number[i]):
                    print("%d " % (i + 1), end="")
            return
        if index == 9:
            return
        for i in range(4):
            self.number[index] = i
            self.dfs(index + 1)

solution = Solution()
for i in range(0, 8, 3):
    solution.start[i], solution.start[i + 1], solution.start[i + 2] = map(int, input().split())
solution.dfs(0)
print("")