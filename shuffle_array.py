import random

class Solution:

    def __init__(self, nums: List[int]):
        self.origin = nums 
        

    def reset(self) -> List[int]:
        return self.origin
        

    def shuffle(self) -> List[int]:
        return random.sample(self.origin, len(self.origin))
