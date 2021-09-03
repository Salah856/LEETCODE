class Solution:
    def isSumEqual(self, firstWord, secondWord, targetWord):
        
        def num(s):
            
            ans = ""
            
            for i in range(len(s)):
                ans += str(ord(s[i]) - ord('a'))
            
            return int(ans)
            
        num1 = num(firstWord)
        num2 = num(secondWord)
        num3 = num(targetWord)
            
        if num1 + num2 == num3:
            return True
        else:
            return False

