class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        
        candyType.sort()
        unique_candies = 1
        
        for i in range(1, len(candyType)):
            
            if candyType[i] != candyType[i - 1]:
                unique_candies += 1
            
            if unique_candies == len(candyType) // 2:
                 break
        
        return min(unique_candies, len(candyType) // 2)
        
