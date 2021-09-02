class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        if len(str(n))<=3:
            return str(n)
        
        s = str(n)
        s = s[::-1]
        l = []
        
        for i in s:
            l.append(i)
            
        i = 3
        while i<len(l):
            l.insert(i,'.')
            i+=4
            
            
        l = l[::-1]
            
        return ''.join(l)
        
