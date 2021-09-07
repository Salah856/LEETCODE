class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        
        def match(item):
            
            if ruleKey == 'color' and item[1] == ruleValue:
                return True 
            
            elif ruleKey == 'type' and item[0] == ruleValue:
                return True
            
            elif ruleKey == 'name' and item[2] == ruleValue:
                return True
            
            else:
                return False 
            
        
        f = filter(match, items)
        l = list(f)
        ll = len(l)
        
        return ll
       
