class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        emails_new = [i.split('@') for i in emails]
        p = []
        
        for i in emails_new:
            
            l = i[0]
            m = l.split('+')
            k = m[0]
            
            n = k.replace('.','')
            f = n + '@' + i[1]
            p.append(f)
        
        return(len(set(p)))
    
    
    
    
    
