from heapq import heappush, heappop

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        n = len(arr)
		
        for i in range(n):
            heappush(heap,(arr[0]/arr[n-1-i],i,0))
        
        while k:
            frac, row, col = heappop(heap)
            if col < n-1-row:
                heappush(heap, (arr[col+1]/arr[n-1-row],row,col+1))
            k -= 1
        
        return [arr[col],arr[n-1-row]]
    
