class Solution(object):
    def areAlmostEqual(self, s1, s2):
        
        if len(s1) != len(s2):
            return False
        
        if s1 == s2:
            return True
        
        lets_a, lets_b = set(), set()
        diff_count = 0
        
        
        for i in range(len(s1)):
            
            if s1[i] != s2[i]:
                
                lets_a.add(s1[i])
                lets_b.add(s2[i])
                
                diff_count += 1
        
        return lets_a == lets_b and diff_count == 2
        
        
