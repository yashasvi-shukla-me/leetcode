"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
"""

#   Using Two Pointers like in 3Sum
#   we don't care about duplicates, we need to return the closest sum

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        close = float('-inf')
        nums.sort()

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:

                curr_sum = nums[i] + nums[left] + nums[right]

                if abs(curr_sum - target) < abs(close - target): 
                    # checking and storing the closest sum to target
                    close = curr_sum

                if curr_sum < target:
                    left = left + 1
                elif curr_sum > target:
                    right = right - 1
                else:
                    return target
        return close