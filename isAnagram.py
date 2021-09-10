class Solution(object):
    def isAnagram(self, s, t):
        
        ss = list(s)
        
        ss.sort()
        
        
        tt = list(t)
        
        tt.sort()
        
        if ss == tt:
            return True 
        
        return False 
        
