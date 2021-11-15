from sortedcontainers import SortedList
from string import digits
from bisect import bisect

class Solution:
    def minInteger(self, num,  k):
        
        d = defaultdict(list)
        ans, seen = [], SortedList()
        
        for i, n in enumerate(num):
            d[n].append(i)
        
        for digit in digits:
            d[digit] = d[digit][::-1]
            
        for i in range(len(num)):
            for digit in digits:
                if d[digit]:
                    index = d[digit][-1]
                    #swap_to_right = len(seen) - bisect(seen,index)
                    swap_to_right = len(seen) - seen.bisect(index)
                    index_after_swap = index + swap_to_right
                    if index_after_swap-i <= k:
                        ans.append(digit)
                        k -= (index_after_swap - i)
                        d[digit].pop()
                        seen.add(index)
                        break
                    
        return "".join(ans)
        
       
