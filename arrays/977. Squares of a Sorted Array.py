"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""

#   Brute Force

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        ls = [x * x for x in nums]
        ls.sort()

        return ls


#   Two Pointers

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        n = len(nums)
        squared = [0] * n
        pos = right = n - 1
        left = 0

        while left <= right:

            if abs(nums[left]) < abs(nums[right]):
                squared[pos] = nums[right] ** 2
                right = right - 1
            else:
                squared[pos] = nums[left] ** 2
                left = left + 1

            pos = pos - 1
            
        return squared