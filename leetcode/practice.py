# -*- coding:utf-8 -*-
import heapq

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        heap = []
        for num in tinput:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                item_min = heap[0]
                if item_min < num:
                    heapq.heapreplace(heap, num)
        return heap