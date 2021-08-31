class Solution:
    
    def getLucky(self, s: str, k: int) -> int:
        
        t = "".join(map(lambda c: str(ord(c) - 96), s))
        
        for _ in range(k):
            
            if len(t) == 1:
                break
            
            t = str(sum(map(int, t)))
        
        return int(t)
