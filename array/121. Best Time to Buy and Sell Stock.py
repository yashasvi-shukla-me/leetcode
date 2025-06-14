"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

#   Brute Force (Basic)
#   Time limit Exceeded on Leetcode

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                maximum = max(maximum, prices[j] - prices[i])
        return maximum


#   Using Kadane's Algorithm

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        minimum = 999999

        for i in prices:
            if i < minimum:
                minimum = i
            else:
                profit = i - minimum
                maximum = max(profit, maximum)
        return maximum


#   A little faster performance (Micro Optimization)
#   Time complexity is same, sometimes executes in less milliseconds

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0

        maximum = 0
        minimum = prices[0]

        for i in prices[1:]:
            minimum = min(i, minimum)
            maximum = max(i - minimum, maximum)
        return maximum