class Codec:
    def __init__(self):
        
        self.num = 0; # create a number as the ID for the shortened URL. 
        
        # Using a number makes conflicts impossible
        
        self.shorttolong = {}; 
        
        # create a dictionary with short URL as keys and long URL as values. 
        # This allows for constant time lookup
    
    def encode(self, longUrl: str) -> str:
        
        """Encodes a URL to a shortened URL.
        """
        n = str(self.num);
        
        self.num += 1; 
        self.shorttolong[n] = longUrl; 
        
        # add key=n (shortURL) and value=longUrl to shorttolong 
        # dictionary for easy decode (constant time)
        
        return n; # return n (the shortURL) 
        
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.shorttolong[shortUrl]; 

    
    
