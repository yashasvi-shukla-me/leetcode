"""
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Example 2:

Input: nums = [1,2,3], k = 0
Output: 0
"""

#   Here the elements of nums are postive and >= 1, so no problem of product 0 or handling (-)ves

#   Using Sliding Window

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        if k <= 1:
            return 0 # small edge case

        prod = 1
        left = 0
        count = 0

        for right in range(len(nums)):
            prod = prod * nums[right]

            while prod >= k:
                prod = prod // nums[left] # shrinking the window
                left = left + 1
            count = count + right - left + 1

        return count