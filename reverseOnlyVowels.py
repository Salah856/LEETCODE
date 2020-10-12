class Solution:
    def reverseVowels(self, s: str) -> str:
        if not s:
            return ""
        letters=list(s)
        n=len(letters)
        vowels={'a','e','i','o','u','A','I','E','O','U'}
        i,j=0,n-1
        while i<j:
            if letters[i] in vowels:
                while letters[j] not in vowels  :
                    j-=1
                   
                letters[i],letters[j]=letters[j],letters[i]
                j-=1
                
            i+=1    
        return ''.join(letters) 
