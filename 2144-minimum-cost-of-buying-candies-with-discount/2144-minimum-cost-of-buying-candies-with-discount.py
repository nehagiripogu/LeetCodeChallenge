class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.sort(reverse=True)
        total = 0
    
        for i in range(len(cost)):
            if i % 3 != 2:  # skip every 3rd candy
                total += cost[i]
    
        return total