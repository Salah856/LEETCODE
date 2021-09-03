class Solution(object):
    
    def findTheDifference(self, s, t):
        
        ds = Counter(s)
        dt = Counter(t)
        
        result = "".join(list((dt - ds).keys()))
        
        return(result)
            
