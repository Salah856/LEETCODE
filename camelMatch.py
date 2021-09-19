class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        
        res = []
        
        for word in queries:
            i = j = 0
            
            while i < len(word):
                if j < len(pattern) and word[i] == pattern[j]:
                    i += 1
                    j += 1
                elif word[i].isupper():
                    break
                else:
                    i += 1
            
            if i == len(word) and j == len(pattern):
                res.append(True)
            
            else:
                res.append(False)
        
        return res
