class Solution:
    def decodeString(self, s: str) -> str:
        
        if not any(map(str.isdigit, s)):
            return s
        
        inner = self.find(s)
        back = s.index(']')
        
        times, val = self.getNumber(s, inner)
        
        string = s[inner+ 1: back]
        s = s.replace(s[val:back+1],string*int(times))
        
        return self.decodeString(s)
    
    def find(self, s):
        
        back = s.index(']')
        front = 0
        
        for i in range(back, 0, -1):
            if s[i] == '[':
                front = i
                break
        
        return front
    
    
    def getNumber(self, s, inner):
        
        ans = ""
        val = 0
        
        for i in range(inner-1,-1, -1):
            if s[i].isdigit():
                ans += s[i]
                val = i
            else:
                break
        
        return ans[::-1], val
    
    
