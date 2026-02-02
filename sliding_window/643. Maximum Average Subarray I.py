"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:

Input: nums = [5], k = 1
Output: 5.00000
"""

#   Brute Force
#   Time limit exceeded

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maximum = float('-inf')

        for i in range(len(nums) - k + 1):
            curr_sum = sum(nums[i:i+k])
            maximum = max(maximum, curr_sum)
        return maximum / k  


#   Using Sliding Window

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_s = sum(nums[:k])
        maximum = window_s

        for i in range(k, len(nums)):
            window_s = window_s + nums[i] - nums[i - k]
            maximum = max(window_s, maximum)
        return maximum/k