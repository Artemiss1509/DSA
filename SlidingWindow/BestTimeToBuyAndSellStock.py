class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = 0

        while right<len(prices):
            if prices[left]>prices[right]:
                left=right
                right=left+1
            else:
                dif = prices[right]-prices[left]
                profit = max(dif,profit)
                right+=1
        
        return profit