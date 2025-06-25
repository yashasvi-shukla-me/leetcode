"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Example 3:

Input: nums = [0,1,1,1,1,1,0,0,0]
Output: 6
Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.
"""

#   Using Prefix Sum and Hash Map

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum_map = {0: -1}   # prefix_sum stored as key & as index stored as value
        prefix_sum = 0
        max_len = 0

        for i in range(len(nums)):
            if nums[i] == 0:    # if number is 0, suppose it as -1
                prefix_sum += -1
            else:
                prefix_sum += 1

            if prefix_sum in sum_map:
                # if that prefix_sum already exists
                # that means after the previous index, sum has again come to zero
                max_len = max(max_len, i - sum_map[prefix_sum])
            else:
                sum_map[prefix_sum] = i

        return max_len