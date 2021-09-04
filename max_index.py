class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        d = {key1 : idx1 for idx1, key1 in enumerate(list1)}
        res = []
        lowest = float('inf')
        
        for idx2, key2 in enumerate(list2):
            
            if key2 in d:
                
                if idx2 + d[key2] == lowest:
                    res.append(key2)
                
                elif idx2 + d[key2] < lowest:
                    res = [key2]
                    lowest = idx2 + d[key2]
        
        return res
