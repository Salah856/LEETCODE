class Solution(object):
    def reversePrefix(self, word, ch):
      
        if not ch in word:
            return word 
        
        i = word.index(ch)
        s = word[ : i+1][::-1]
        d = word[ i+1 : ] 
        
        return s + d
        
        
