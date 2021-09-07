class Solution(object):
    def arrangeWords(self, text):
        splittedText = text.split()
        sortedText = sorted(splittedText, key = len)
        joinedSorted = " ".join(sortedText)
        loweredJoinedSortedText = joinedSorted.lower()
        
        return loweredJoinedSortedText[0].upper() + loweredJoinedSortedText[1:]
    
    
