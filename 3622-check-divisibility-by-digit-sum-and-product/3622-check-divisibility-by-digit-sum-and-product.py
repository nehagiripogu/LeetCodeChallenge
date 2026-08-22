class Solution:
    def checkDivisibility(self, n: int) -> bool:
        strr=str(n)
        summ=0
        prod=1
        for i in range(len(strr)):
            summ+=int(strr[i])
            prod*=int(strr[i])
        return n % (summ + prod) == 0