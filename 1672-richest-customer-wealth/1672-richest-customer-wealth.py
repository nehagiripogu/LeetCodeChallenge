class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        richest = 0

        for customer in accounts:

            wealth = sum(customer)

            if wealth > richest:
                richest = wealth

        return richest