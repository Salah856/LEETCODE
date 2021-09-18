class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        
        if len(sentence2)>len(sentence1):
            return self.areSentencesSimilar(sentence2,sentence1)
        
        sentence1=sentence1.split(" ")
        sentence2=sentence2.split(" ")
        
        s1=sentence1[:]
        s2=sentence2[:]
        
        while s1[0]==s2[0]:
                s1.pop(0)
                s2.pop(0)
                if not s2:
                    return True
        
        if not s2:
            return True
        
        while s1[-1]==s2[-1]:
                s1.pop()
                s2.pop()
                if not s2:
                    return True
        
        if not s2:
            return True
        
        return False
