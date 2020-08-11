# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if numbers == None or numbers == []: return None
        if len(numbers) == 1: return numbers[0]
        # find the medium
        res = self.findTheMedium(numbers, 0, len(numbers) - 1)
        
        cnt = 0
        for num in numbers:
            if num == res:
                cnt += 1
        return res if cnt > len(numbers) >> 1 else 0
    
    def findTheMedium(self, numbers, start, end):
        medium = len(numbers) >> 1
        index = self.partion(numbers, start, end)
        while index != medium:
            if index > medium and start < index - 1:
                index = self.partion(numbers, start, index - 1)
            elif index < medium and index + 1 < end:
                index = self.partion(numbers, index + 1, end)
        return numbers[index]
    
    def partion(self, numbers, start, end):
        pivot = numbers[start]
        while start < end:
            while start < end and numbers[end] >= pivot: end -= 1
            numbers[start] = numbers[end]
            while start < end and numbers[start] <= pivot: start += 1
            numbers[end] = numbers[start]
        numbers[start] = pivot
        return start