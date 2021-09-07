class Solution:
    def minNumberOfFrogs(self, A: str) -> int:
        
        counter = Counter(A)
		
        # Pruning: string should contain 
        # all the 5 characters of "croak" and 
        # no other characters. Each character should appear the same times
        
        if len(counter) != 5 or sum(s not in "croak" for s in counter) or len(set(counter.values())) != 1:
            return -1
        
        dp = [0] * 5
        res = 0
        
        for s in A:
            
            idx = "croak".index(s)
            dp[idx] += 1
            
            for prev in range(idx):
                if dp[prev] < dp[idx]:
                    return -1
            
            if s == "c":
                res = max(res, dp[0] - dp[-1])
        
        return res
                              
