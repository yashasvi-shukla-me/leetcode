"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""

#   Brute Force Approach

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        return (nums.index(target) if target in nums else -1)


#   Linear Search

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
    
    
#   Binary Search (Optimal)

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1
        return -1