class StreamChecker(object):

    def __init__(self, words):
        
        self.words = words
        self.lacc = ""
        self.ws = "".join(self.words)
        

    def query(self, letter):
        if not letter in self.ws:
            return False 
        
        
        if letter in self.ws:
            self.lacc += letter
            
        for word in self.words:
            
            if self.lacc == word:
                self.lacc = ""
                return True
        
        
        return False
    
    
                
  
