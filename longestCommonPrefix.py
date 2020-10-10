class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix=[]
        num = len(strs)
        
        for x in zip(*strs):
            if len(set(x)) == 1:
                prefix.append(x[0])
            else:
                break
                
                
        return "".join(prefix)
        
