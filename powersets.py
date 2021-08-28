def powerset(array):
    subsets = [[]]
    
    for el in array:
        for i in range(len(subsets)):
            currentSubset = subsets[i]
            subsets.append(currentSubset + [el])
    
    return subsets
  
