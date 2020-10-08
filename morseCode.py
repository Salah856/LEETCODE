class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
       
       c = ["a","b",
       "c","d",
       "e","f",
       "g","h",
       "i","j",
       "k","l", 
       "m","n",
       "o","p",
       "q","r",
       "s","t",
       "u",
       "v","w",
       "x",
       "y","z"]
       
       v = [".-","-...","-.-.","-..",
       ".","..-.","--.","....","..",
       ".---","-.-",
       ".-..","--","-.",
       "---",".--.","--.-",".-.","...",
       "-","..-","...-",
       ".--","-..-","-.--","--.." ]
        
        return len(set(map(lambda x:"".join([v[c.index(j)]for j in x]),words)))
