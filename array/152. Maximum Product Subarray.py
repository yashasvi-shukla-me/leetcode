"""
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

#   Brute Force Approach
#   Time limit exceeded for large size array

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maximum = nums[0]

        for i in range(n):
            prod = 1
            for j in range(i, n):
                prod = prod * nums[j]
                maximum = max(prod, maximum)
        return maximum


#   Kadane's Algorithm (Optimal Approach)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = min_prod = result = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            prev_max = max_prod

            max_prod = max(num, num * max_prod, num * min_prod)
            min_prod = min(num, num * prev_max, num * min_prod)

            result = max(result, max_prod)

        return result