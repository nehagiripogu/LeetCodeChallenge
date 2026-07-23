class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        subset=[]
        def backtrack(i):
            if len(subset)==k and sum(subset)==n:
                res.append(subset[:])
                return
            for j in range(i,10):
                subset.append(j)
                backtrack(j+1)
                subset.pop()
        backtrack(1)
        return res