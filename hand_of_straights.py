import collections

class Solution:    
    def __init__(self):
        self.groups = collections.deque()
    
    def _fit(self, v: int):
        
        if self.groups and v - self.groups[0][-1] > 1:
             raise ValueError()
                
        for group in self.groups:
            if v - group[-1] == 1:
                group.append(v)
                break
        else:
            self.groups.append([v])
            
    
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        hand.sort()
        for v in hand:
            try:
                self._fit(v)
            except ValueError:
                return False
            
            group = self.groups[0]
            if len(group) == W:
                print(self.groups.popleft())
        
        return len(self.groups) == 0
