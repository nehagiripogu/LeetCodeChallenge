class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res=[]
        subset=[]
        def backtrack(start):
            if len(subset)==k:
                res.append(subset[:])
                return
            for i in range(start,n+1):
                subset.append(i)
                backtrack(i+1)
                subset.pop()
        backtrack(1)
        return res
        