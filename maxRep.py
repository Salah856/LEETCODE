class Solution:
    def maxRepOpt1(self, text: str) -> int:
                
        d = dict(Counter(text))
        
        x = None
        chars = []
        amounts = []
        
        for c in text:
            if c == x:
                amounts[-1] += 1
            else:
                chars.append(c)
                amounts.append(1)
            
            x = c
        
        ans = max( min(amounts[0]+1, d[chars[0]]), min(amounts[-1]+1, d[chars[-1]]) )
            
        for i in range(1, len(chars)-1):       
            
            if amounts[i] == 1 and chars[i-1] == chars[i+1]:
                ans = max(ans, min(amounts[i-1] + amounts[i+1] + 1, d[chars[i-1]]) )
                        
            ans = max(min(amounts[i]+1, d[chars[i]]), ans)
            
        
        return ans
