from collections import Counter

def solution(A):
    # write your code in Python 3.6
    
    items = Counter(A).items()
    res = []

    for k, v in items:
        if v == 1:
            res.append(A.index(k))
    
    return A[min(res)] if len(res) > 0 else -1 
