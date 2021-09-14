class Solution(object):
    def maximumUnits(self, A, truckSize):
        res = 0
        maxUnits = max(units for _, units in A)
        count = [0] * (maxUnits + 1)
        
        for boxes, units in A:
            count[units] += boxes
        
        i = len(count) - 1
        
        while i and truckSize:
            if count[i]:
                boxesToAdd = min(truckSize, count[i])
                res += i * boxesToAdd
                count[i] -= boxesToAdd
                truckSize -= boxesToAdd
            i -= 1
        
        return res

        
