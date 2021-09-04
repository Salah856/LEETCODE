class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn == 0: return ["0:00"]
        
        res = []
        mapping = [1,2,4,8,16,32,1,2,4,8] # 10 elements with 6 digits of minuts and 4 digits of hours
        choose = [False]*11 # to remember which digit has been chosen

        def backtrack(idx,curOn,curH,curM):
            
            if curH > 11 or curM > 59 or choose[curOn]: # invalid choice 
                return
            
            if idx ==0:
                res.append("%d:%02d"%(curH, curM))
                return
            

            for i in range(curOn,10):
                choose[i] = True # mark the chosen digit to true
                if i > 5:
                    backtrack(idx-1, i+1, curH+mapping[i],curM)
                else:
                    backtrack(idx-1, i+1, curH, curM+mapping[i])
                choose[i] = False 
                
        backtrack(turnedOn,0,0,0)
        
        return res
