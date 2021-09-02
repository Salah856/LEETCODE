class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()
        s.sort()
        
        #Sorting the two arrays so we can use two pointer algorithm on them
        
        i = 0
        j = 0
        ret = 0
        
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                
                # if the greed factor of a particular child is less than the corresponding
                # cookie, then he/she will be happy
                # And hence move on to next cookie and child
                
                ret = ret + 1
                i = i + 1
                j = j + 1
            
            else:
                # if a child has more greedy factor than the corresponding cookie
                # We move on to next cookie, but same child so i will be same
                
                j = j + 1
        
        return ret
