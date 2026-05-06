class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res=0
        i=0
        j=len(heights)-1
        while i<j:
            width=j-i
            height=min(heights[i],heights[j])
            vol=width*height
            res=max(res,vol)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return res
