class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter
        freq=Counter(words)
        res=[ word for word,val in sorted(freq.items(),key = lambda x :(-x[1],x[0]))]
        return res[:k]