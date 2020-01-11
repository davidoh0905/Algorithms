"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

## Brute Force

class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        for i in range(0, len(prices) - 1):
            for j in range(i + 1, len(prices)):
                temp = prices[j] - prices[i]
                if (temp > profit):
                    profit = temp
        return profit


print(Solution().maxProfit([7, 20, 3, 6, 1, 2, 1, 1]))

## Alex

class Solution(object):
    def maxProfit(self, prices):
        sellingPrice = 0
        buyingPrice = prices[0]
        profit = 0
        for i in range(1, len(prices) - 1):
            if (prices[i] < buyingPrice):
                buyingPrice = prices[i]
                sellingPrice = 0
            if (prices[i] > sellingPrice):
                sellingPrice = prices[i]
            profit = max(profit, sellingPrice - buyingPrice)
        return profit


print(Solution().maxProfit([7, 20, 3, 6, 1, 2, 1, 1]))


## Alex 1 : First of all, if the algorithm is given, I should congnitively approach it and solve it by using brute force and then try to develop the algorithm with greater efficiency.

# David

class Solution(object):
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0

        current = prices[0]
        leastSoFar = float("inf")
        maxSoFar = 0
        for i in range(len(prices)):
            current = prices[i]
            maxSoFar = max(maxSoFar, current - leastSoFar)
            leastSoFar = min(leastSoFar, current)
        return maxSoFar
























