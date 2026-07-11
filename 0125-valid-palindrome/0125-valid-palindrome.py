class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.strip()
        res=''
        for s in s:
            if s.isalnum():
                res+=s
        left=0
        right=len(res)-1
        res=res.lower()
        if len(res)==1:
            return True
        while left<right:
            if res[left]!=res[right]:
                return False
            left+=1
            right-=1
        return True