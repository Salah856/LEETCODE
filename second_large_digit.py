class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=[]
        
        for i in s:
            if i.isnumeric():
                res.append(i)
        
        res1 = set(res)
        
        if len(res1) < 2:
            return -1
        
        else:
            return sorted(res1)[-2]
        
