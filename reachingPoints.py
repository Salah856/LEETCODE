class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx <= tx and sy <= ty:
            if tx == sx and ty == sy: return True
            if tx == ty: break
            if tx > ty:
                tx %= ty
            elif ty > tx:
                ty %= tx
            
            if tx == sx: # only change ty
                if (ty-sy) % sx ==0:
                    return True
                else:
                    return False 
                
            if ty == sy: # only change tx
                if (tx-sx) % sy == 0:
                    return True
                else:
                    return False 
        return False 
