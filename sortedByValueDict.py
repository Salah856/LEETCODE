from collections import Counter

class Solution(object):
    def frequencySort(self, s):
        
        items = Counter(s).items()

        res = ""

        sortedItems = sorted(items, key=lambda x: x[1], reverse=True)

        for k, v in sortedItems:
            res += (v * k)


        return res


            
            
        
