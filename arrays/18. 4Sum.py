"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
"""

#   Using Two Pointers

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        quad = []
        nums.sort()
        n = len(nums)

        # i and j are the two numbers of quadruplets
        # left and right are the other two

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue # skipping duplicates
            
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue # skipping duplicates

                left, right = j + 1, n - 1

                while left < right:

                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        quad.append([nums[i], nums[j], nums[left], nums[right]])
                        left = left + 1
                        right = right - 1

                        while left < right and nums[left] == nums[left - 1]:
                            left = left + 1 # checking until diff value for left
                        while left < right and nums[right] == nums[right + 1]:
                            right = right - 1 # checking until diff value for right
                    elif total < target:
                        left = left + 1
                    else:
                        right = right - 1
        return quad