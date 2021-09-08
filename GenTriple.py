
def GenTriple(n):
    n_squared = n ** 2
    squares = set([ x ** 2 for x in range(1, n + 1)])
    diffs = [n_squared-sqr for sqr in squares]
    present = [diff in squares for diff in diffs]
    
    return sum(present) 

class Solution:
    def countTriples(self, n):
        
        trips = [GenTriple(x) for x in range(1,n+1)]
        
        return sum(trips)
