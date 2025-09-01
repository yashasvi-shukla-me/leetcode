"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""

#   Using Two Pointers

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        triplets = []

        for i in range(len(nums) - 2): # our first number is nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1 # next two number of triplets

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:  # if triplet found add numbers in list
                    triplets.append([nums[i], nums[left], nums[right]])
                    left = left + 1
                    right = right - 1

                    while left < right and nums[left] == nums[left - 1]:
                        left = left + 1  # checking for duplicates
                    while left < right and nums[right] == nums[right + 1]:
                        right = right - 1  # checking for duplicates

                elif total < 0:
                    left = left + 1
                else:
                    right = right - 1

        return triplets