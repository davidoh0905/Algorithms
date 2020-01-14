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
    def productExceptSelf(self, nums):
        ## In order to get productExceptSelf at index i,
        ## we need to get product of every element of nums before index i
        ## and multiply that with product of every element of nums after index i
        ## we will create auxiliary array as L and R
        L, R, answer = [1] * len(nums), [1] * len(nums), [1] * len(nums)

        for i in range(1, len(nums)):
            # left to right
            # ith element of L is product of L[i-1] (product of every element until i-2 th element from left) and nums[i-1]
            L[i] = L[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            # right to left
            # ith element of R is product of R[i+1] (product of every element until i+2 th element from right) and nums[i+1]
            R[i] = R[i + 1] * nums[i + 1]

        for i in range(len(nums)):
            answer[i] = L[i] * R[i]

        return answer

    ## This leaves us room for improvement in that we can just use one auxiliary data structure.
    ## 
























