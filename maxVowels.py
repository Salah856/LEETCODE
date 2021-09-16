class Solution(object):
    def maxVowels(self, s, k):   
        vowels = 0
        for i in range(k):
            if s[i] in "aeiou": vowels += 1
        
        maxVowels = vowels
        
        for i in range(k, len(s)):
            
            if s[i] in "aeiou":
                vowels += 1
            
            if s[i-k] in "aeiou":
                vowels -= 1
    
            maxVowels = max(maxVowels, vowels)
        
        return maxVowels
            
            
            
