class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        maxx=0
        while i<j:
            width=j-i
            h=min(heights[i],heights[j])
            area=width*h
            maxx=max(area,maxx)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return maxx