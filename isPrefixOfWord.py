class Solution:
    def isPrefixOfWord(self, sentence, searchWord):
        
        s = sentence.split()
        
        for i,w in enumerate(s, 1):
            if w.startswith(searchWord): return i
        
        return -1
