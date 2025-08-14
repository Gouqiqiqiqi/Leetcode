'''
Question 121: Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

'''

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Initialize the minimum price to a very high value and maximum profit to 0
        if not prices:
            return 0
        min_price = price[0] # This set min_price to positive infinity
        # This is done to ensure that any price in the list will be less than this initial value.
        max_profit = 0

        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
        return max_profit

price = [7, 1, 5, 3, 6, 4]
s = Solution()
print(s.maxProfit(price))  # Output: 5 (Buy on day 2 and sell on day 5)


'''
The logic to solve the problem is as follows:
1. find the minimum price in the list of prices.
2. find the maximum profit by subtracting the minimum price from the current price.
3. If the current price is less than the minimum price, update the minimum price.
4. Return the maximum profit after iterating through all prices.
'''

'''
#min(x, y):
The function min(x, y) is a built-in Python function that simply returns the smaller of the two values x and y.
i.e.
min(3, 5)  # returns 3
min(10, 2) # returns 2
min(-1, -5) # returns -5

#max(x, y):
The function max(x, y) is a built-in Python function that returns the larger of the two values x and y.
i.e.
max(3, 5)  # returns 5
max(10, 2) # returns 10
max(-1, -5) # returns -1

'''

'''
How min_price = min(min_price, i) works:

Current i	Previous min_price	New min_price = min(min_price, i)
7	        inf	                min(inf, 7) → 7
1	        7	                min(7, 1) → 1
5	        1	                min(1, 5) → 1
3	        1	                min(1, 3) → 1
6	        1	                min(1, 6) → 1
4	        1	                min(1, 4) → 1


how max_profit = max(max_profit, i - min_price) works:
Current i	Previous max_profit	Current min_price	New max_profit = max(max_profit, i - min_price)
7	        0	                7	                max(0, 7 - 7) → 0
1	        0	                1	                max(0, 1 - 1) → 0
5	        0	                1	                max(0, 5 - 1) → 4
3	        4	                1	                max(4, 3 - 1) → 4
6	        4	                1	                max(4, 6 - 1) → 5
4	        5	                1	                max(5, 4 - 1) → 5

'''




'''
if not some_value:
    # Do something if some_value is falsy

The 'if not...' statement in Python is a shorthand way to check if something is empty or False.

i.e.
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
if not prices: checks if the prices list is empty. If it is, the function returns 0 immediately, indicating that no profit can be made.
'''


'''
Mistakes I made:

Mistake 1:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit = 0
        min_price = prices[0]

        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(0, prices[i] - min_price)
        return max_profit

This version is wrong because it lacks memory.

The code correctly calculates a potential profit on each day, 
but it immediately overwrites the max_profit variable in every loop iteration 
instead of keeping track of the best profit found so far.


Mistake 2:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        max_price = 0

        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            max_price = max(max_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
        return max_profit

The error in the code is a logical flaw: 
it doesn't ensure that the stock is bought before it's sold.
The code tracks the absolute minimum price (min_price) 
and the absolute maximum price (max_price) seen up to the current day 
and calculates the profit from their difference.

This is incorrect because the maximum price might have occurred before 
the minimum price. 
'''