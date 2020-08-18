# -*- coding:utf-8 -*-
class Solution:
    def quickSort(self, arr, left, right):
        if left < right:
            index = self.partion(arr, left, right)
            self.quickSort(arr, left, index)
            self.quickSort(arr, index + 1, right)
    
    def partion(self, arr, left, right):
        pivot = arr[left]
        while left < right:
            while left < right and arr[right] <= pivot: right -= 1
            arr[left] = arr[right]
            while left < right and arr[left] >= pivot: left += 1
            arr[right] = arr[left]
        arr[left] = pivot
        return left