class Solution(object):
    def defangIPaddr(self, address):
        
        to_replace = '.'
        replaced = '[.]'
        new_string = ''
        
        for elem in address:
            
            if elem == to_replace:
                new_string += replaced
            
            else:
                new_string += elem
        
        return new_string
