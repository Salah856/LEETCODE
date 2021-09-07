class Solution:
    def reorderSpaces(self, text: str) -> str:
        
        t, spaces = text.split(), text.count(" ")
        
        not_spaces = len(t)
        
        if spaces == 0:
            return text
        
        if not_spaces == 1:
            return text.strip() + " " * spaces

        ratio, left = divmod(spaces, (not_spaces - 1))
        
        return (" " * ratio).join(t) + " " * left
    
    
    
    
    
