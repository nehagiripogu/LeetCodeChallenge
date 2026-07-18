class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        maxlen=0
        freq={}
        for right in range(len(s)):
            freq[s[right]]=freq.get(s[right],0)+1
            while freq.get(s[right],0)>1:
                freq[s[left]] -= 1
                left+=1
            
            maxlen=max(maxlen,right-left+1)
        return maxlen