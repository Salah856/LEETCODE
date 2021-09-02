class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        
        accounts_sum = []
        
        
        for account in accounts:
            accounts_sum.append(sum(account))
        
        
        return max(accounts_sum)
            
