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

#   Brute Force Approach

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = sorted([x*x for x in nums])
        return result


#   Using Two Pointers 

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        # array is sorted which helps
        # pos is for putting values in squares array
        
        n = len(nums)
        left = 0
        right = n - 1
        pos = n - 1
        squares = [0] * n # array of zeroes

        while left <= right:

            if abs(nums[left]) > abs(nums[right]): # simple if u think about it
                squares[pos] = nums[left] ** 2
                left = left + 1
            else:
                squares[pos] = nums[right] ** 2
                right = right - 1
            pos = pos - 1
        return squares