class Solution:
    def totalMoney(self, n: int) -> int:
        
        total = 0
        weeks = (n) // 7
        
        for w in range(weeks):
            total += 28 + 7 * (w)
        
        remainder = n % 7
        curr = 1 + weeks
        
        for d in range(remainder):
            
            total += curr
            curr += 1
        
        
        return total
