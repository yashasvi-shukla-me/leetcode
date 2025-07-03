"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
"""

#   Sliding Window (Optimal)

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimum = 999999
        left = 0
        window_sum = 0

        for right in range(len(nums)):
            window_sum = window_sum + nums[right]

            while window_sum >= target:

                minimum = min(minimum, right - left + 1)
                window_sum = window_sum - nums[left]
                left = left + 1

        if minimum == 999999:
            return 0
        return minimum