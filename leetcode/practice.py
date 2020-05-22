# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        def __init__(self):
            self.ans = 0
            
        def MergeSort(self, arr, low, high):
            if low < high:
                mid = (low + high) >> 1
                self.MergeSort(self, arr, low, mid)
                self.MergeSort(self, arr, mid+1, high)
                self.Merge(self, arr, low, mid, high)
        
        def Merge(self, arr, low, mid, high):
            temp = [0]*(high-low+1)
            i = 0
            p1, p2 = low, mid+1
            while p1 <= mid and p2 <= high:
                if arr[p1] > arr[p2]:
                    self.ans += mid - p1 + 1
                    temp[i] = arr[p2]
                    i += 1; p2 += 1
                else:
                    temp[i] = arr[p1]
                    i += 1; p1 += 1
            while p1 <= mid: temp[i] = arr[p1]; i += 1; p1 += 1
            while p2 <= high: temp[i] = arr[p2]; i += 1; p2 += 1
            arr[low:high+1] = temp[:]
        
        MergeSort(data, 0, len(data)-1);
        return self.ans