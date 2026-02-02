"""
Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.

A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

Return the maximum length of a subarray with positive product.

Example 1:

Input: nums = [1,-2,-3,4]
Output: 4
Explanation: The array nums already has a positive product of 24

Example 2:

Input: nums = [0,1,-2,-3,-4]
Output: 3
Explanation: The longest subarray with positive product is [1,-2,-3] which has a product of 6.
Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.

Example 3:

Input: nums = [-1,-2,-3,0,1]
Output: 2
Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].
"""

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        max_len = count_neg = start = 0
        first_neg = -1

        for i in range(len(nums)):
            if nums[i] == 0:
                start = i + 1
                first_neg = -1
                count_neg = 0
            else:
                if nums[i] < 0:
                    count_neg += 1
                    if first_neg == -1:
                        first_neg = i
                         
                if count_neg % 2 == 0:
                    max_len = max(max_len, i - start + 1)
                else:
                    max_len = max(max_len, i - first_neg)
        return max_len