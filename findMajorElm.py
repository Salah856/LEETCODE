from collections import Counter
import math 

def findMajorityElement(arr, n):
    
    c = Counter(arr)
    items = c.items()
    
    for k, v in items:
        if v > math.floor(n / 2):
            return k
    
    return -1
