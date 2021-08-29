def kadanesAlgorithm(array):
    
    maxEndingHere = array[0]
    maxSoFar = array[0]
    
    for i in range(1, len(array)):
        num = array[i]
        maxEndingHere = max(num, maxEndingHere + num)
        maxSoFar = max(maxSoFar, maxEndingHere)
    
    return maxSoFar
  
  
  
