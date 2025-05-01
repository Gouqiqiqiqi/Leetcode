'''
Question:

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time.
However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.
'''

#This question wants to find the sum of all gains in the prices array.

#The key point in this problem is you can buy and sell on the same day.


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0

        for i in range(1, len(prices)):
            profit = prices[i] - prices[i - 1]
            max_profit += max(profit, 0)
        return max_profit
    

prices = [7, 1, 5, 3, 6, 4]
solution = Solution()
result = solution.maxProfit(prices)
print(result)


'''
The logic behind this question:
1. Find the difference between the current price and the previous price.
2. If the difference is positive, add it to the max_profit.
3. If the difference is negative, ignore it.
4. Return the max_profit.
'''