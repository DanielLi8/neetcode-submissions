class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0

        maxP= 0
        left =0
        right = 1
        for i in range(len(prices)-1):
            
            if prices[left]>prices[right]:
                left= right
            else:
                maxP= max(maxP, prices[right]-prices[left])
            right+=1

        return maxP
