class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=['a','e','i','o','u']
        window=s[:k]
        maxvow=0
        res=[]
        for ch in window:
            if ch in vowels:
                maxvow+=1
        res.append(maxvow)
        for i in range(k,len(s)):
            if s[i-k] in vowels:
                maxvow-=1
            if s[i] in vowels:
                maxvow+=1
            res.append(maxvow)
        return max(res)