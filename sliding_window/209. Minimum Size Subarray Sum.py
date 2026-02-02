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

#   Sliding Window Approach
#   Time Complexity: O(n), Space Complexity: O(1)

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        minimal = float('inf')
        left = 0
        windowSum = 0

        for right in range(len(nums)):

            windowSum += nums[right]

            while windowSum >= target:

                minimal = min(minimal, right - left + 1)
                windowSum -= nums[left]
                left += 1

        return 0 if minimal == float('inf') else minimal