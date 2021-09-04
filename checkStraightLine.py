class Solution(object):
    def checkStraightLine(self, coordinates):

        if len(coordinates)<=2: return True
        
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        
        Xdiff, Ydiff = x1 - x2 , y1 - y2
        
        for x,y in coordinates[2:]:
            
            if Ydiff * (x1 - x) != (y1 - y) * Xdiff:
                return False
        
        return True
    
    
