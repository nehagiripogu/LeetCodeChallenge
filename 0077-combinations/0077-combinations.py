class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums=[]
        for i in range(n):
            nums.append(i+1)
        res=[]
        subset=[]
        def backtrack(i):
            if len(subset)==k:
                res.append(subset[:])
                return
            for j in range(i,len(nums)):
                subset.append(nums[j])
                backtrack(j+1)
                subset.pop()
        backtrack(0)
        return res