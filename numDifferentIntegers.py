class Solution(object):
    def numDifferentIntegers(self, word):
        
        l = len(word)
        wrd = ""
        
        for i in range(l):
            if word[i].isalpha():
                wrd += " "
            else:
                wrd += word[i]

        w = wrd.split()

        d = [] 

        for i in w:
            if i.isnumeric():
                d.append(int(i))


        return len(set(d))
