class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        windowsum=sum(arr[:k])
        maxx=[]
        maxx.append(windowsum/k)
        for i in range(k,len(arr)):
            windowsum-=arr[i-k]
            windowsum+=arr[i]
            maxx.append(windowsum/k)
        count=0
        for i in maxx:
            if i>=threshold:
                count+=1
        return count