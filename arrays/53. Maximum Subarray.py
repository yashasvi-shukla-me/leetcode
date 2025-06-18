"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
"""

#   Brute Force
#   Time limit exceeded for large input sizes

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maximum = float('-inf')

        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum = curr_sum + nums[j]
                maximum = max(maximum, curr_sum)
        return maximum


#   Kadane's Algorithm (Optimal Approach)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = curr_sum = nums[0]

        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            maximum = max(maximum, curr_sum)
        return maximum


#   Optimized for faster speed

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = curr_sum = nums[0]
        for i in range(1, len(nums)):
            val = nums[i]
            curr_sum = val if curr_sum < 0 else curr_sum + val
            max_sum = max(max_sum, curr_sum)
        return max_sum