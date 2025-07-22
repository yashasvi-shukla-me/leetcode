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


#   Modified Kadane's Algorithm

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        curr_max = curr_min = max_prod = nums[0]

        for i in range(1, len(nums)):

            num = nums[i]

            if num < 0: # check if it' negative
                curr_max, curr_min = curr_min, curr_max # multiplying with a negative flips the sign
            curr_max = max(num, num * curr_max)
            curr_min = min(num, num * curr_min)

            max_prod = max(max_prod, curr_max)

        return max_prod   