class Solution:
    def maxArea(self, heights: List[int]) -> int:

        res = []
        l = 0
        r = len(heights)-1

        while l<r:

            height = r - l
            width = min(heights[l],heights[r])
            area = height * width
            res.append(area)

            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        
        return max(res)







        