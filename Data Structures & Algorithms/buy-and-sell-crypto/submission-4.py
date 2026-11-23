class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = 0
        r = 1
        p = []

        while r<len(prices):
            if prices[l]<prices[r]:
                diff = prices[r] - prices[l]
                p.append(diff)
            else:
                l =r 
            r+=1

        return max(p) if p else 0       
