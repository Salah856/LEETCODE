class Solution:
    def thousandSeparator(self, n: int) -> str:
        n_str = [each for each in str(n)]    
        for i in range(len(n_str)-3,0, -3):
          n_str.insert(i, ".")
        return "".join(n_str)
    
    
