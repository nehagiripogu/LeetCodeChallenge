from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq=Counter(magazine)
        flag=True
        for ch in ransomNote:
            if freq[ch]==0:
                return False
            else:
                freq[ch]-=1               
        return True 