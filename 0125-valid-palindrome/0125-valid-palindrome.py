class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.strip().lower()
        res=''
        for ch in s:
            if ch.isalnum():
                res+=ch
        j=len(res)-1
        i=0
        while i<j:
            if res[i]!=res[j]:
                return False
            i+=1
            j-=1
        return True