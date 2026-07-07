class Solution:
    def sumAndMultiply(self, n: int) -> int:
        n=str(n)
        res=''
        for num in n:
            if int(num)!=0:
                res+=(num)
        sum=0
        if res=='':
            return 0
        for s in res:
            sum+=int(s)
        res=int(res)


        return res*sum
