from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:    
        freq=Counter(s)
        res=''
        for key,value in sorted(freq.items(),key=lambda x:x[1],reverse=True):
            res+=key*value
        return res