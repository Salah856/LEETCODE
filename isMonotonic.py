class Solution(object):
    def isMonotonic(self, A):
        
        increasing = decreasing = True
        l = len(A)

        for i in xrange(l - 1):
            if A[i] > A[i+1]:
                increasing = False
            if A[i] < A[i+1]:
                decreasing = False

        return increasing or decreasing
